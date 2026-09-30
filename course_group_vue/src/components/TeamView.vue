<script setup>
import {computed, onMounted, ref} from 'vue'
import api from '../api'

// 加载状态
const loading = ref(true)
const loadingFaculty = ref(true)
const loadingStudents = ref(true)
const loadingAssistants = ref(true)

// 教师团队数据
const facultyMembers = ref([])

// 研究生数据
const graduateStudents = ref([])

// 毕业校友数据
const graduate = ref([])

// 图片加载超时时间（毫秒）
const IMG_LOAD_TIMEOUT = 5000 // 5秒超时

// 获取团队成员数据
const fetchTeamData = async () => {
  try {
    // 从API获取组织结构数据
    const data = await api.getOrganization()

    // 处理并分类成员数据
    const processedFaculty = data
        .filter(m => ['head', 'professor', 'associate_professor'].some(role => m.role === role))
        .map(m => ({
          ...m,
          avatarText: m.name.substring(0, 1),
          researchDetails: m.specialty ? m.specialty.split('、') : [],
          education: [],
          publications: [],
          imgLoaded: false, // 图片加载状态
          imgTimeout: null // 超时定时器
        }))

    const processedStudents = data.filter(member =>
        member.role === 'phd' || member.role === 'master' || member.role === 'undergraduate' || member.role === 'postdoctoral'
    ).map(m => ({
      ...m,
      avatarText: m.name.substring(0, 1),
      degree: m.role === 'phd' ? '博士研究生' : m.role === 'master' ? '硕士研究生' : m.role === 'undergraduate' ? '本科生' : '博士后',
      category: m.role === 'phd' ? '博士研究生' : m.role === 'master' ? '硕士研究生' : m.role === 'undergraduate' ? '本科生' : '博士后',
      researchArea: m.specialty || '',
      imgLoaded: false,
      imgTimeout: null
    }))

    const processedGraduate = data.filter(member =>
        member.role === 'graduate'
    )

    facultyMembers.value = processedFaculty
    graduateStudents.value = processedStudents
    graduate.value = processedGraduate
  } catch (error) {
    console.error('获取团队成员数据失败:', error)
  } finally {
    loadingFaculty.value = false
    loadingStudents.value = false
    loadingAssistants.value = false
    loading.value = false
  }
}

// 学生分类和当前选中的标签
const studentCategories = ['全部', '博士研究生', '硕士研究生', '本科生']
const activeTab = ref('全部')

// 模态框状态
const showModal = ref(false)
const selectedMember = ref(null)

// 根据选中的标签过滤学生
const filteredStudents = computed(() => {
  if (activeTab.value === '全部') {
    return graduateStudents.value
  }
  return graduateStudents.value.filter(student => student.category === activeTab.value)
})

// 显示成员详情
const showMemberDetail = (member) => {
  // 重置图片加载状态和超时器
  selectedMember.value = {...member, imgLoaded: false, imgTimeout: null}
  showModal.value = true
}

// 关闭模态框
const closeModal = () => {
  // 清除模态框成员的超时器
  if (selectedMember.value?.imgTimeout) {
    clearTimeout(selectedMember.value.imgTimeout)
  }
  showModal.value = false
  selectedMember.value = null
}

// 图片加载超时处理
const handleImgTimeout = (member) => {
  member.avatar = ''
  member.imgLoaded = false
}

// 图片加载失败处理
const handleImgError = (member) => {
  // 清除超时器
  if (member.imgTimeout) {
    clearTimeout(member.imgTimeout)
  }
  member.avatar = ''
  member.imgLoaded = false
}

// 图片加载完成处理
const handleImgLoad = (member) => {
  // 清除超时器
  if (member.imgTimeout) {
    clearTimeout(member.imgTimeout)
  }
  member.imgLoaded = true
}

// 初始化图片加载超时器
const initImgTimeout = (member) => {
  // 仅当有图片链接时设置超时
  if (member.avatar && member.avatar.trim()) {
    member.imgTimeout = setTimeout(() => {
      handleImgTimeout(member)
    }, IMG_LOAD_TIMEOUT)
  }
}

// 组件挂载时获取数据
onMounted(() => {
  fetchTeamData().then(() => {
    // 为所有成员初始化图片超时器
    facultyMembers.value.forEach(initImgTimeout)
    graduateStudents.value.forEach(initImgTimeout)
  })
})
</script>

<template>
  <div class="team-view">
    <!-- 页面标题 -->
    <div class="page-header">
      <h1>研究团队</h1>
      <p>我们拥有一支由优秀学者和研究人员组成的跨学科团队</p>
    </div>

    <!-- 教师团队 -->
    <div class="container section">
      <h2 class="section-title">教师团队</h2>
      <div v-if="loadingFaculty" class="loading">加载中...</div>
      <div v-else class="member-grid faculty-grid">
        <div class="member-card" v-for="member in facultyMembers" :key="member.id">
          <!-- 头像容器：解决图片文字重叠问题 + 超时控制 -->
          <div class="member-avatar">
            <!-- 图片容器：有图片时显示，无图片时隐藏 -->
            <div class="avatar-img-wrapper" v-if="member.avatar && member.avatar.trim()">
              <img
                  class="avatar-img"
                  :src="member.avatar"
                  :alt="member.name"

                  @error="handleImgError(member)"
                  @load="handleImgLoad(member)"
                  v-show="member.imgLoaded"
              />
              <!-- 加载中动画（超时后自动消失） -->
              <div v-if="!member.imgLoaded" class="avatar-loading">
                <span class="loading-icon">●</span>
              </div>
            </div>
            <!-- 文字占位：无图片/超时/加载失败时显示 -->
            <div v-else class="avatar-placeholder">{{ member.avatarText }}</div>
          </div>

          <div class="member-info">
            <h3 class="member-name">{{ member.name }}</h3>
            <p class="member-title">{{ member.title }}</p>
            <p class="member-email">{{ member.email }}</p>
            <p class="member-research">{{ member.researchArea }}</p>
            <div class="member-actions">
              <button class="btn btn-secondary" @click="showMemberDetail(member)">查看详情</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 学生团队 -->
    <div class="container section">
      <h2 class="section-title">学生团队</h2>
      <div v-if="loadingStudents" class="loading">加载中...</div>
      <div class="member-tabs">
        <button
            v-for="category in studentCategories"
            :key="category"
            class="tab-button"
            :class="{ active: activeTab === category }"
            @click="activeTab = category"
        >
          {{ category }}
        </button>
      </div>
      <div class="member-grid student-grid">
        <div
            class="member-card student-card"
            v-for="student in filteredStudents"
            :key="student.id"
        >
          <!-- 头像容器 -->
          <div class="member-avatar student-avatar">
            <div class="avatar-img-wrapper" v-if="student.avatar && student.avatar.trim()">
              <img
                  class="avatar-img"
                  :src="student.avatar"
                  :alt="student.name"
                  @error="handleImgError(student)"
                  @load="handleImgLoad(student)"
                  v-show="student.imgLoaded"
              />
              <div v-if="!student.imgLoaded" class="avatar-loading">
                <span class="loading-icon">●</span>
              </div>
            </div>
            <div v-else class="avatar-placeholder">{{ student.avatarText }}</div>
          </div>

          <div class="member-info student-info">
            <h3 class="member-name">{{ student.name }}</h3>
            <p class="member-title">{{ student.title }}</p>
            <p class="member-email">{{ student.email }}</p>
            <p class="member-research">{{ student.researchArea }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 毕业校友 -->
    <div class="container section">
      <h2 class="section-title">毕业校友</h2>
      <div class="alumni-table-container">
        <table class="alumni-table">
          <thead>
          <tr>
            <th>姓名</th>
            <th>本科/硕士/博士</th>
            <th>研究成果</th>
            <th>毕业去向</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="graduate in graduate" :key="graduate.id">
            <td>{{graduate.name}}</td>
            <td>{{graduate.title}}</td>
            <td>{{graduate.research_result}}</td>
            <td>{{graduate.graduation_destination}}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 成员详情模态框 -->
    <div class="modal" v-if="showModal" @click.self="closeModal">
      <div class="modal-content">
        <button class="close-button" @click="closeModal">&times;</button>
        <div class="modal-header">
          <!-- 模态框头像 -->
          <div class="member-avatar large-avatar">
            <div class="avatar-img-wrapper" v-if="selectedMember?.avatar && selectedMember.avatar.trim()">
              <img
                  class="avatar-img"
                  :src="selectedMember.avatar"
                  :alt="selectedMember.name"
                  @error="handleImgError(selectedMember)"
                  @load="handleImgLoad(selectedMember)"
                  v-show="selectedMember.imgLoaded"
              />
              <!-- 初始化模态框图片超时器 -->
              <div v-if="!selectedMember.imgLoaded" class="avatar-loading" @mounted="initImgTimeout(selectedMember)">
                <span class="loading-icon">●</span>
              </div>
            </div>
            <div v-else class="avatar-placeholder">{{ selectedMember?.avatarText }}</div>
          </div>

          <div>
            <h2 class="modal-title">{{ selectedMember?.name }}</h2>
            <p class="modal-subtitle">{{ selectedMember?.title }}</p>
          </div>
        </div>
        <div class="modal-body">
          <div class="info-section">
            <h3>联系信息</h3>
            <p><strong>联系电话：</strong>{{ selectedMember?.phone }}</p>
            <p><strong>邮箱：</strong>{{ selectedMember?.email }}</p>
            <p><strong>办公室：</strong>{{ selectedMember?.office }}</p>
          </div>
          <div class="info-section">
            <h3>研究方向</h3>
            <p>{{ selectedMember?.researchArea }}</p>
            <div v-if="selectedMember?.researchDetails && selectedMember.researchDetails.length > 0">
              <ul>
                <li v-for="(detail, index) in selectedMember.researchDetails" :key="index">{{ detail }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.team-view {
  min-height: 100vh;
  background-color: #f8f9fa;
}

/* 页面标题样式 */
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

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section {
  padding: 60px 0;
}

.section-title {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 40px;
  text-align: center;
  position: relative;
}

.section-title::after {
  content: '';
  display: block;
  width: 100px;
  height: 4px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  margin: 15px auto 0;
  border-radius: 2px;
}

/* 成员网格布局 */
.member-grid {
  display: grid;
  gap: 30px;
}

.faculty-grid {
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
}

.student-grid {
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
}

.assistant-grid {
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
}

/* 成员卡片样式 */
.member-card {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  padding: 25px;
  display: flex;
  align-items: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.member-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.student-card {
  flex-direction: column;
  align-items: center;
  text-align: center;
}

/* 头像核心样式：解决重叠问题 */
.member-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 30px;
  flex-shrink: 0;
  overflow: hidden;
  position: relative;
}

/* 图片容器：仅在有图片时渲染 */
.avatar-img-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
}

/* 头像图片 */
.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

/* 加载中动画 */
.avatar-loading {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.loading-icon {
  font-size: 16px;
  color: white;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* 文字占位：仅无图片时显示 */
.avatar-placeholder {
  color: white;
  font-size: 2.5rem;
  font-weight: bold;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 学生/助手头像样式调整 */
.student-avatar {
  margin-right: 0;
  margin-bottom: 20px;
}

/* 模态框大头像 */
.large-avatar {
  width: 150px;
  height: 150px;
}

.large-avatar .avatar-placeholder {
  font-size: 4rem;
}

.large-avatar .loading-icon {
  font-size: 20px;
}

/* 成员信息样式 */
.member-info {
  flex: 1;
}

.student-info, .assistant-info {
  text-align: center;
}

.member-name {
  font-size: 1.5rem;
  color: #2c3e50;
  margin: 0 0 8px 0;
}

.member-title {
  font-size: 1.1rem;
  color: #667eea;
  margin: 0 0 8px 0;
  font-weight: 500;
}

.member-email {
  color: #666;
  margin: 0 0 8px 0;
  font-size: 0.95rem;
}

.member-research {
  color: #555;
  margin: 0 0 15px 0;
  line-height: 1.6;
}

/* 按钮样式 */
.member-actions {
  margin-top: 15px;
}

.btn {
  padding: 8px 20px;
  border: none;
  border-radius: 6px;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary {
  background-color: #667eea;
  color: white;
}

.btn-secondary:hover {
  background-color: #764ba2;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

/* 学生标签页 */
.member-tabs {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 40px;
}

.tab-button {
  padding: 10px 30px;
  border: none;
  background-color: #f0f4ff;
  color: #666;
  border-radius: 30px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.tab-button:hover {
  background-color: #e0e7ff;
}

.tab-button.active {
  background-color: #667eea;
  color: white;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

/* 模态框样式 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background-color: white;
  border-radius: 12px;
  padding: 40px;
  max-width: 800px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.close-button {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 2rem;
  background: none;
  border: none;
  cursor: pointer;
  color: #666;
  transition: color 0.3s ease;
}

.close-button:hover {
  color: #333;
}

.modal-header {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f4ff;
}

.modal-header > div:last-child {
  margin-left: 30px;
}

.modal-title {
  font-size: 2rem;
  color: #2c3e50;
  margin: 0 0 8px 0;
}

.modal-subtitle {
  font-size: 1.2rem;
  color: #667eea;
  margin: 0;
}

.modal-body {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.info-section h3 {
  font-size: 1.3rem;
  color: #2c3e50;
  margin: 0 0 15px 0;
  padding-bottom: 8px;
  border-bottom: 1px solid #e0e7ff;
}

.info-section p {
  margin: 0 0 10px 0;
  line-height: 1.7;
  color: #555;
}

.info-section ul {
  padding-left: 20px;
  margin: 15px 0;
}

.info-section li {
  margin-bottom: 8px;
  color: #555;
  line-height: 1.6;
}

.edu-item, .pub-item {
  margin-bottom: 15px;
  padding: 12px;
  background-color: #f8f9fa;
  border-radius: 6px;
  border-left: 4px solid #667eea;
}

.pub-item {
  font-size: 0.95rem;
  line-height: 1.6;
}

/* 响应式设计 */
.loading {
  text-align: center;
  padding: 3rem;
  color: #666;
  font-size: 1.2rem;
}

/* 毕业校友表格样式 */
.alumni-table-container {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  padding: 30px;
  overflow-x: auto;
}

.alumni-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 1rem;
}

.alumni-table th {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 15px;
  text-align: left;
  font-weight: 600;
  border: none;
}

.alumni-table td {
  padding: 15px;
  border-bottom: 1px solid #f0f4ff;
  color: #555;
}

.alumni-table tr:nth-child(even) {
  background-color: #f8f9fa;
}

.alumni-table tr:hover {
  background-color: #f0f4ff;
  transition: background-color 0.3s ease;
}

@media (max-width: 768px) {
  .page-header {
    padding: 60px 0;
  }

  .page-header h1 {
    font-size: 2rem;
  }

  .section {
    padding: 40px 0;
  }

  .faculty-grid {
    grid-template-columns: 1fr;
  }

  .member-card {
    flex-direction: column;
    text-align: center;
  }

  .member-avatar {
    margin-right: 0;
    margin-bottom: 20px;
  }

  .member-tabs {
    flex-direction: column;
    align-items: center;
  }

  .tab-button {
    width: 200px;
  }

  .modal-content {
    padding: 30px 20px;
    margin: 10px;
  }

  .modal-header {
    flex-direction: column;
    text-align: center;
  }

  .modal-header > div:last-child {
    margin-left: 0;
    margin-top: 20px;
  }

  .large-avatar {
    width: 120px;
    height: 120px;
  }

  .large-avatar .avatar-placeholder {
    font-size: 3rem;
  }

  .alumni-table-container {
    padding: 20px;
  }

  .alumni-table th,
  .alumni-table td {
    padding: 10px;
    font-size: 0.9rem;
  }
}
</style>