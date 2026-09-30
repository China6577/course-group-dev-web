<script setup>
import {onMounted, ref, watch, nextTick} from 'vue'
import api from '../api'

const loading = ref(true)
const publications = ref([]) // 原始全量论文数据
const filteredPublications = ref([]) // 筛选后的所有数据（未分页）

// 分页相关响应式数据
const currentPage = ref(1) // 当前页码
const pageSize = ref(10) // 每页显示10条
const total = ref(0) // 筛选后数据的总条数
const paginatedPublications = ref([]) // 当前页要展示的分页数据

// 论文类型筛选
const publicationTypes = ref([
  {value: 'all', label: '全部论文'},
  {value: 'conference', label: '会议论文'},
  {value: 'journal', label: '期刊论文'},
  {value: 'other', label: '其他'}
])
const selectedType = ref('all')

// 年份筛选
const years = ref([{value: 'all', label: '全部年份'}])
const selectedYear = ref('all')

// 关键字搜索
const searchKeyword = ref('')

// 摘要展开状态管理
const expandedAbstracts = ref(new Set())

// 摘要长度阈值
const abstractMaxLength = 150

// 弹窗状态管理
const showBibtexModal = ref(false)
const currentBibtex = ref('')
const currentPub = ref(null)

// 弹窗引用
const bibtexModalDiv = ref(null)

// 切换摘要展开状态
const toggleAbstract = (pubId) => {
  if (expandedAbstracts.value.has(pubId)) {
    expandedAbstracts.value.delete(pubId)
  } else {
    expandedAbstracts.value.add(pubId)
  }
}

// 检查摘要是否需要截断
const isAbstractTooLong = (abstract) => {
  return abstract.length > abstractMaxLength
}

// 获取截断后的摘要
const getTruncatedAbstract = (abstract) => {
  if (abstract.length <= abstractMaxLength) {
    return abstract
  }
  return abstract.substring(0, abstractMaxLength) + '...'
}

// 打开 BibTeX 弹窗
const openBibtexModal = (pub) => {
  currentPub.value = pub
  currentBibtex.value = pub.bibtex_text
  showBibtexModal.value = true

  // 弹窗打开后自动聚焦到 div 标签上
  nextTick(() => {
    if (bibtexModalDiv.value) {
      bibtexModalDiv.value.focus()
    }
  })
}

// 关闭 BibTeX 弹窗
const closeBibtexModal = () => {
  showBibtexModal.value = false
  currentPub.value = null
  currentBibtex.value = ''
}

// 复制 BibTeX 到剪贴板
const copyBibtex = async () => {
  try {
    await navigator.clipboard.writeText(currentBibtex.value)
    alert('BibTeX copied to clipboard!')
  } catch (err) {
    console.error('Failed to copy BibTeX:', err)
    alert('Failed to copy BibTeX. Please try again.')
  }
}

// 打开论文链接
const openPaperLink = (pub) => {
  if (pub.paper_url) {
    window.open(pub.paper_url, '_blank')
  } else {
    alert('No paper URL available for this publication.')
  }
}

// 获取论文数据
const fetchPublications = async () => {
  try {
    loading.value = true
    // 获取全量数据
    publications.value = await api.getPublications()
    // 提取所有年份并去重
    const uniqueYears = [...new Set(publications.value.map(pub => pub.year))]
    // 按年份降序排序
    uniqueYears.sort((a, b) => b - a)
    // 更新年份选项
    years.value = [{value: 'all', label: '全部年份'}]
    uniqueYears.forEach(year => {
      years.value.push({value: year.toString(), label: year.toString()})
    })
    // 先筛选，再分页
    filterPublications()
  } catch (error) {
    console.error('获取论文数据失败:', error)
  } finally {
    loading.value = false
  }
}

// 筛选论文（筛选后更新分页）
const filterPublications = () => {
  filteredPublications.value = publications.value.filter(pub => {
    // 类型筛选
    const typeMatch = selectedType.value === 'all' || pub.type === selectedType.value
    // 年份筛选
    const yearMatch = selectedYear.value === 'all' || pub.year.toString() === selectedYear.value
    // 关键字搜索（搜索标题、作者、摘要）
    const keywordMatch = !searchKeyword.value ||
        (pub.title && pub.title.toLowerCase().includes(searchKeyword.value.toLowerCase())) ||
        (pub.authors && pub.authors.toLowerCase().includes(searchKeyword.value.toLowerCase())) ||
        (pub.abstract && pub.abstract.toLowerCase().includes(searchKeyword.value.toLowerCase()))
    return typeMatch && yearMatch && keywordMatch
  })
  // 筛选后重置页码为1，重新计算分页
  currentPage.value = 1
  calculatePagination()
}

// 计算分页数据
const calculatePagination = () => {
  // 总条数
  total.value = filteredPublications.value.length
  // 计算当前页数据：起始索引 = (当前页-1)*每页条数，结束索引 = 起始索引+每页条数
  const startIndex = (currentPage.value - 1) * pageSize.value
  const endIndex = startIndex + pageSize.value
  paginatedPublications.value = filteredPublications.value.slice(startIndex, endIndex)
  // 重置展开状态
  expandedAbstracts.value.clear()
}

// 切换页码
const changePage = (page) => {
  // 边界校验：页码不能小于1，不能大于总页数
  if (page < 1 || page > Math.ceil(total.value / pageSize.value)) return
  currentPage.value = page
}

// 监听筛选条件变化（可选：防止手动修改selectedType时未触发筛选）
watch(selectedType, filterPublications)
watch(selectedYear, filterPublications)
watch(searchKeyword, filterPublications)
// 监听当前页码变化，重新计算分页
watch(currentPage, calculatePagination)

// 组件挂载时获取数据
onMounted(() => {
  fetchPublications()
})
</script>

<template>
  <div class="publications">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="container">
        <h1>发表论文</h1>
        <p>课题组最新研究成果和学术论文</p>
      </div>
    </div>

    <div class="container">
      <!-- 筛选区域 -->
      <div class="filter-section">
        <div class="filter-item">
          <label>论文类型：</label>
          <select v-model="selectedType" @change="filterPublications">
            <option v-for="type in publicationTypes" :key="type.value" :value="type.value">
              {{ type.label }}
            </option>
          </select>
        </div>
        <div class="filter-item">
          <label>发表年份：</label>
          <select v-model="selectedYear" @change="filterPublications">
            <option v-for="year in years" :key="year.value" :value="year.value">
              {{ year.label }}
            </option>
          </select>
        </div>
        <div class="filter-item search-box">
          <label>关键字：</label>
          <input
              type="text"
              v-model="searchKeyword"
              placeholder="搜索标题、作者或摘要"
              @input="filterPublications"
          >
        </div>
      </div>

      <!-- 论文列表 -->
      <div class="publications-list">
        <div v-if="loading" class="loading">加载中...</div>
        <div v-else-if="!paginatedPublications.length" class="empty">暂无相关论文数据</div>
        <div v-else>
          <div v-for="pub in paginatedPublications" :key="pub.id" class="publication-item card">
            <h2><a :href="pub.paper_url">{{ pub.title }}</a></h2>
            <p class="authors">{{ pub.authors }}</p>
            <p class="venue">
              {{ pub.venue }}, {{ pub.year }}
            </p>
            <div class="abstract">
              <h3>摘要</h3>
              <p>
                {{ expandedAbstracts.has(pub.id) ? pub.abstract : getTruncatedAbstract(pub.abstract) }}
              </p>
            </div>

            <!-- 操作按钮区域（展开按钮和论文操作按钮放在同一排） -->
            <div class="publication-actions">
              <button
                  v-show="isAbstractTooLong(pub.abstract)"
                  class="abstract-toggle-btn"
                  @click="toggleAbstract(pub.id)"
              >
                {{ expandedAbstracts.has(pub.id) ? '收起' : '展开' }}
              </button>
              <div class="action-buttons">
                <button
                    class="action-btn paper-btn"
                    @click="openPaperLink(pub)"
                >
                  <span class="btn-icon">📄</span>
                  Paper
                </button>
                <button
                    class="action-btn bibtex-btn"
                    @click="openBibtexModal(pub)"
                >
                  <span class="btn-icon">📚</span>
                  BibTeX
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 分页组件 -->
      <div v-if="total > pageSize" class="pagination">
        <!-- 上一页 -->
        <button
            class="page-btn"
            :disabled="currentPage === 1"
            @click="changePage(currentPage - 1)"
        >
          上一页
        </button>

        <!-- 页码显示 -->
        <span class="page-info">
          第 {{ currentPage }} 页 / 共 {{ Math.ceil(total / pageSize) }} 页
          （总 {{ total }} 条）
        </span>

        <!-- 下一页 -->
        <button
            class="page-btn"
            :disabled="currentPage === Math.ceil(total / pageSize)"
            @click="changePage(currentPage + 1)"
        >
          下一页
        </button>
      </div>
    </div>

    <!-- BibTeX 导出弹窗 -->
    <div v-if="showBibtexModal" class="bibtex-modal-overlay" @click.self="closeBibtexModal"
         @keyup.esc="closeBibtexModal" tabindex="-1" ref="bibtexModalDiv">
      <div class="bibtex-modal">
        <div class="bibtex-modal-header">
          <h3>Export Citations</h3>
          <button class="close-btn" @click="closeBibtexModal">&times;</button>
        </div>
        <div class="bibtex-modal-body">
          <pre class="bibtex-code">{{ currentBibtex }}</pre>
        </div>
        <div class="bibtex-modal-footer">
          <button class="copy-btn" @click="copyBibtex">Copy</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* 页面头部样式 */
.page-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 80px 0;
  text-align: center;
}

.page-header h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.page-header p {
  font-size: 1.2rem;
  opacity: 0.9;
  max-width: 800px;
  margin: 0 auto;
}

.publications {
  padding-bottom: 60px;
}

.loading, .empty {
  text-align: center;
  padding: 3rem;
  color: #666;
  font-size: 1.2rem;
}

.filter-section {
  margin: 40px 0 30px;
  display: flex;
  gap: 20px;
  align-items: center;
  flex-wrap: wrap;
}

.filter-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.filter-item label {
  font-weight: bold;
  white-space: nowrap;
}

.filter-item select,
.filter-item input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  min-width: 150px;
}

.filter-item.search-box input {
  min-width: 300px;
}

@media (max-width: 768px) {
  .filter-section {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .filter-item {
    width: 100%;
  }

  .filter-item select,
  .filter-item input {
    flex: 1;
    min-width: unset;
  }

  .filter-item.search-box input {
    min-width: unset;
  }
}

.publications-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 30px;
}

.publication-item {
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.publication-item h2 {
  margin-bottom: 10px;
  color: #2c3e50;
  font-size: 20px;
}

.authors {
  color: #3498db;
  margin-bottom: 5px;
  font-weight: bold;
}

.venue {
  color: #7f8c8d;
  margin-bottom: 15px;
  font-style: italic;
}

.abstract h3 {
  margin-bottom: 10px;
  font-size: 16px;
  color: #2c3e50;
}

.abstract p {
  color: #555;
  line-height: 1.6;
  margin-bottom: 10px;
}

.abstract-toggle-btn {
  background: none;
  border: none;
  color: #3498db;
  font-size: 14px;
  font-weight: bold;
  cursor: pointer;
  padding: 0;
  margin-top: 5px;
  transition: color 0.3s ease;
}

.abstract-toggle-btn:hover {
  color: #2980b9;
  text-decoration: underline;
}

/* 论文操作按钮样式 */
.publication-actions {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 20px;
}

.action-buttons {
  display: flex;
  gap: 10px;
  margin-left: auto;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f8f9fa;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn:hover {
  background-color: #e9ecef;
  border-color: #adb5bd;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.btn-icon {
  font-size: 16px;
}

.paper-btn {
  color: #495057;
}

.bibtex-btn {
  color: #495057;
}

/* 摘要展开按钮样式调整 */
.abstract-toggle-btn {
  background: none;
  border: none;
  color: #3498db;
  font-size: 14px;
  font-weight: bold;
  cursor: pointer;
  padding: 0;
  margin: 0;
  transition: color 0.3s ease;
}

.abstract-toggle-btn:hover {
  color: #2980b9;
  text-decoration: underline;
}

/* BibTeX 弹窗样式 */
.bibtex-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.bibtex-modal {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  width: 90%;
  max-width: 800px;
  max-height: 80vh;
  overflow: hidden;
}

.bibtex-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid #e9ecef;
  background-color: #f8f9fa;
}

.bibtex-modal-header h3 {
  margin: 0;
  font-size: 18px;
  font-weight: bold;
  color: #2c3e50;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #6c757d;
  padding: 0;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.close-btn:hover {
  background-color: #e9ecef;
}

.bibtex-modal-body {
  padding: 20px;
  max-height: 50vh;
  overflow-y: auto;
}

.bibtex-code {
  background-color: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  padding: 16px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  line-height: 1.4;
  white-space: pre-wrap;
  margin: 0;
  color: #495057;
}

.bibtex-modal-footer {
  padding: 20px;
  border-top: 1px solid #e9ecef;
  background-color: #f8f9fa;
  display: flex;
  justify-content: flex-end;
}

.copy-btn {
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.copy-btn:hover {
  background-color: #2980b9;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .bibtex-modal {
    width: 95%;
    margin: 20px;
  }

  .bibtex-modal-header,
  .bibtex-modal-body,
  .bibtex-modal-footer {
    padding: 15px;
  }

  .bibtex-code {
    font-size: 13px;
    padding: 12px;
  }
}

/* 分页样式 */
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  padding: 20px 0;
}

.page-btn {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: #fff;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.page-btn:disabled {
  cursor: not-allowed;
  color: #999;
  background: #f5f5f5;
  border-color: #eee;
}

.page-btn:not(:disabled):hover {
  background: #3498db;
  color: #fff;
  border-color: #3498db;
}

.page-info {
  color: #666;
  font-size: 14px;
}

/* 响应式样式 */
@media (max-width: 768px) {
  .page-header {
    padding: 60px 0;
  }

  .page-header h1 {
    font-size: 2rem;
  }

  .page-header p {
    font-size: 1rem;
  }

  .publication-item h2 {
    font-size: 18px;
  }
}
</style>