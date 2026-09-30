<script setup>
import {onMounted, ref} from 'vue'
import api from '../api'

// 加载状态
const loading = ref(true)

// 合作伙伴数据
const partners = ref([])

// 组件挂载时获取数据
onMounted(async () => {
  loading.value = true
  try {
    // 获取合作伙伴数据
    partners.value = await api.getPartners()
  } catch (error) {
    console.error('获取合作伙伴数据失败:', error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="partners">
    <!-- 页面头部 -->
    <div class="page-header">
      <h1>合作伙伴</h1>
      <p>与我们携手合作的机构和企业</p>
    </div>

    <div class="container">
      <div v-if="loading" class="loading">加载中...</div>
      <div v-else>
        <div class="partners-grid">
          <div v-for="partner in partners" :key="partner.id || partner.name" class="partner-card">
            <img v-if="partner.logo" :src="partner.logo" :alt="partner.name" class="partner-logo">
            <h3 class="partner-name">{{ partner.name }}</h3>
            <p class="partner-description">{{ partner.description }}</p>
            <a v-if="partner.website" :href="partner.website" target="_blank" class="partner-link">访问官网</a>
          </div>
          <p v-if="partners.length === 0">暂无合作伙伴信息</p>
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

.partners {
  padding-bottom: 60px;
}

/* 加载样式 */
.loading {
  text-align: center;
  padding: 3rem;
  color: #666;
  font-size: 1.2rem;
}

/* 合作伙伴样式 */
.partners-grid {
  margin-top: 40px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
}

.partner-card {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  padding: 30px 20px;
  text-align: center;
  transition: all 0.3s ease;
  border: 1px solid #f0f0f0;
}

.partner-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: #e0e0e0;
}

.partner-logo {
  max-width: 180px;
  max-height: 100px;
  width: auto;
  height: auto;
  margin: 0 auto 20px;
  display: block;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.partner-card:hover .partner-logo {
  transform: scale(1.05);
}

.partner-name {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 12px;
}

.partner-description {
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 0.95rem;
  min-height: 60px;
}

.partner-link {
  display: inline-block;
  padding: 8px 20px;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.partner-link:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
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

  .partners-grid {
    grid-template-columns: 1fr;
  }
}
</style>