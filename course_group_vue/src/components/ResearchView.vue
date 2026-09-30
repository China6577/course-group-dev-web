<script setup>
import {onMounted, ref} from 'vue'
import api from '../api'

const researchAreas = ref([])
const loading = ref(true)

onMounted(async () => {
  loading.value = true
  try {
    // 从API获取研究领域数据
    researchAreas.value = await api.getResearchDirections()
  } catch (error) {
    console.error('获取研究领域数据失败:', error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="research">
    <!-- 页面标题 -->
    <div class="page-header">
      <h1>研究领域</h1>
      <p>探索我们在人工智能与文化交叉领域的研究重点</p>
    </div>

    <div class="container">
      <!-- 加载状态 -->
      <div v-if="loading" class="loading">加载中...</div>

      <!-- 研究领域列表 -->
      <div v-else class="research-grid">
        <div v-for="area in researchAreas" :key="area.id" class="research-card card">
          <div class="research-header">
            <h2>{{ area.name }}</h2>
          </div>
          <div class="research-content">
            <p class="research-brief">{{ area.details || '' }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.research {
  min-height: 100vh;
  background-color: #f8f9fa;
}

.loading {
  text-align: center;
  padding: 3rem;
  color: #666;
  font-size: 1.2rem;
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

/* 研究领域网格 */
.research-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 40px;
  padding: 60px 0;
}

/* 研究卡片样式 */
.research-card {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.research-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.research-header {
  padding: 20px 25px 15px;
  border-bottom: 2px solid #3498db;
}

.research-header h2 {
  margin: 0 0 10px 0;
  color: #667eea;
  font-size: 1.5rem;
}

.research-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
}

.research-leader {
  color: #666;
}

.research-progress {
  background-color: #e0e0e0;
  color: #666;
  padding: 3px 12px;
  border-radius: 20px;
  font-weight: 500;
}

.research-progress.progress-active {
  background-color: #667eea;
  color: white;
}

.research-content {
  padding: 25px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.research-brief {
  font-weight: bold;
  margin-bottom: 15px;
  color: #2c3e50;
  font-size: 1.1rem;
}

/* 研究要点 */
.research-points {
  margin-bottom: 20px;
}

.research-points h3 {
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 10px;
}

.research-points ul {
  margin: 0;
  padding-left: 20px;
}

.research-points li {
  margin-bottom: 8px;
  color: #555;
}

/* 研究成果 */
.research-achievements {
  margin-bottom: 20px;
}

.research-achievements h3 {
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 10px;
}

.achievements-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.achievement-item {
  background-color: #f8f9fa;
  padding: 10px 15px;
  border-radius: 6px;
  border-left: 4px solid #667eea;
  font-size: 0.95rem;
  line-height: 1.5;
}

/* 研究团队 */
.research-team {
  margin-bottom: 20px;
}

.research-team h3 {
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 10px;
}

.team-members {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.team-member {
  background-color: #667eea;
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
}

/* 研究图片 */
.research-image {
  margin-top: auto;
  height: 180px;
  background-color: #f0f0f0;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.image-placeholder {
  color: #999;
  font-size: 16px;
  text-align: center;
  padding: 20px;
}

/* 研究合作部分样式已删除 */

/* 响应式设计 */
@media (max-width: 768px) {
  .page-header {
    padding: 60px 0;
  }

  .page-header h1 {
    font-size: 2rem;
  }

  .research-grid {
    grid-template-columns: 1fr;
    padding: 40px 0;
    gap: 30px;
  }

  .research-meta {
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
  }

  .collaboration-section {
    padding: 60px 0;
  }

  .collaboration-options {
    grid-template-columns: 1fr;
  }
}
</style>