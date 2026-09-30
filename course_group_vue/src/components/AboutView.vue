<script setup>
import {ref, onMounted, computed, onUnmounted} from 'vue'
import api from '../api'

const allNews = ref([])
const researchAreas = ref([])
const loading = ref(true)
const showAll = ref(false)

// 轮播图相关
const currentSlide = ref(0)
const slideInterval = ref(null)
const slides = ref([
  {
    title: '关于我们',
    subtitle: '人工智能赋能文化传承与创新',
    description: '我们期待优秀的博士、硕士研究生和研究助理加入我们团队'
  },
  {
    title: '研究愿景',
    subtitle: '融人文科技，领文化智能创新',
    description: '推动人文与科技深度融合，引领文化智能技术创新'
  },
  {
    title: '合作邀请',
    subtitle: '开放合作，共促发展',
    description: '欢迎与国内外高校、研究机构和企业建立合作关系'
  }
])

const startSlideInterval = () => {
  slideInterval.value = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.value.length
  }, 5000)
}

const stopSlideInterval = () => {
  if (slideInterval.value) {
    clearInterval(slideInterval.value)
    slideInterval.value = null
  }
}

const goToSlide = (index) => {
  currentSlide.value = index
}

const fetchData = async () => {
  loading.value = true
  try {
    // // 获取所有新闻
    // const newsData = await api.getNews()
    // const processedNews = newsData
    //     // 只显示要发布的新闻
    //     .filter(item => item.is_published)
    //     // 日期降序 即最新的在前面
    //     .sort((a, b) => new Date(b.publish_date) - new Date(a.publish_date))
    //     .map(item => ({
    //       // item对象的属性不变
    //       ...item,
    //       // 格式化覆盖item对象的date属性 中文格式的本地日期字符串
    //       date: new Date(item.publish_date).toLocaleDateString('zh-CN')
    //     }))

    // 获取研究方向
    const allAreas = await api.getResearchDirections()
    const processedAreas = allAreas
        // 按照order属性升序
        .sort((a, b) => (a.order || 0) - (b.order || 0))
        // 在home页面只显示三个主要的研究方向
        // .slice(0, 3)

    // allNews.value = processedNews
    researchAreas.value = processedAreas
  } catch (error) {
    console.error('获取数据失败:', error)
  } finally {
    loading.value = false
  }
}

// 计算显示的新闻：最多5条，或全部
const displayNews = computed(() => {
  if (showAll.value) {
    return allNews.value
  }
  return allNews.value.slice(0, 5)
})

// 切换显示全部/收起
const toggleShowAll = () => {
  showAll.value = !showAll.value
}

onMounted(() => {
  fetchData()
  startSlideInterval()
})

onUnmounted(() => {
  stopSlideInterval()
})
</script>

<template>
  <div class="home">
    <!-- 轮播图英雄区域 -->
    <section class="hero-carousel">
      <div class="carousel-container">
        <div
            class="carousel-slides"
            :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
        >
          <div
              v-for="(slide, index) in slides"
              :key="index"
              class="carousel-slide"
          >
            <div class="container">
              <h1>{{ slide.title }}</h1>
              <p class="subtitle">{{ slide.subtitle }}</p>
              <p class="description">{{ slide.description }}</p>
            </div>
          </div>
        </div>

        <!-- 轮播指示器 -->
        <div class="carousel-indicators">
          <button
              v-for="(slide, index) in slides"
              :key="index"
              class="indicator"
              :class="{ active: currentSlide === index }"
              @click="goToSlide(index)"
              @mouseenter="stopSlideInterval"
              @mouseleave="startSlideInterval"
          ></button>
        </div>
      </div>
    </section>

    <!-- 简介区域 -->
    <section class="research-areas">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">简介</h2>
        </div>
        <div class="areas-grid">
          <div class="area-card card">
            <p>
              以“AI赋能文化”为核心，聚焦原创性基础研究与应用研究。紧扣国家文化数字化战略和文化产业需求，基于AI算法与多模态大模型，攻克行业适配性、研究系统性、应用整体性、文化独特性等关键问题，推动文化数字化从理论突破到工程应用，再到产业转化的全链条发展。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 研究方向区域 -->
    <section class="research-areas">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">主要研究领域</h2>
          <router-link to="/research" class="view-more">查看详情</router-link>
        </div>
        <div v-if="loading" class="loading">加载中...</div>
        <div v-else class="areas-grid">
          <div v-for="area in researchAreas" :key="area.id" class="area-card card">
            <h3>{{ area.name }}</h3>
            <p>{{ area.description }}</p>
          </div>
        </div>
      </div>
    </section>

<!--    &lt;!&ndash; 最新动态区域 &ndash;&gt;-->
<!--    <section class="news">-->
<!--      <div class="container">-->
<!--        <div class="section-header">-->
<!--          <h2 class="section-title">最新动态</h2>-->
<!--          <button @click="toggleShowAll" class="view-more">-->
<!--            {{ showAll ? '收起' : '查看全部' }}-->
<!--          </button>-->
<!--        </div>-->
<!--        <div v-if="loading" class="loading">加载中...</div>-->
<!--        <div v-else class="news-list">-->
<!--          <div v-for="item in displayNews" :key="item.id" class="news-item">-->
<!--            <div class="news-date">{{ item.date }}</div>-->
<!--            <div class="news-content">-->
<!--              <h3>{{ item.title }}</h3>-->
<!--              <p>{{ item.description }}</p>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </section>-->
  </div>
</template>

<style scoped>
.loading {
  text-align: center;
  padding: 2rem;
  color: #666;
  font-size: 1.1rem;
}

.hero-carousel {
  position: relative;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  margin-bottom: 0;
  overflow: hidden;
}

.carousel-container {
  position: relative;
  width: 100%;
  height: 400px;
}

.carousel-slides {
  display: flex;
  height: 100%;
  transition: transform 0.5s ease-in-out;
}

.carousel-slide {
  flex: 0 0 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-slide .container {
  text-align: center;
  padding: 0 20px;
}

.carousel-slide h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.subtitle {
  font-size: 24px;
  margin-bottom: 30px;
  opacity: 0.9;
}

.description {
  font-size: 18px;
  max-width: 800px;
  margin: 0 auto 40px;
  opacity: 0.9;
}

.carousel-indicators {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.indicator.active {
  background-color: white;
  width: 30px;
  border-radius: 6px;
}

.indicator:hover {
  background-color: rgba(255, 255, 255, 0.8);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.view-more {
  color: #3498db;
  text-decoration: none;
  font-weight: bold;
  font-size: 16px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  font-family: inherit;
}

.view-more:hover {
  text-decoration: underline;
}

.cta {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.btn-secondary {
  background-color: transparent;
  border: 2px solid white;
}

.btn-secondary:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.research-areas {
  background-color: #f9f9f9;
  padding: 40px 0;
  margin-top: 0;
  margin-bottom: 0;
}

.areas-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
}

.area-card h3 {
  color: #2c3e50;
  margin-bottom: 15px;
  font-size: 20px;
}

.area-card.card p {
  font-size: 18px;
  line-height: 1.6;
  color: #333;
}

.news {
  background-color: #f9f9f9;
  padding: 40px 0;
  margin-top: 0;
}

.news-item {
  display: flex;
  margin-bottom: 30px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.news-date {
  background-color: #3498db;
  color: white;
  padding: 20px;
  text-align: center;
  min-width: 120px;
}

.news-content {
  padding: 20px;
  flex: 1;
}

.news-content h3 {
  margin-bottom: 10px;
  font-size: 20px;
}

/* 卡片样式 */
.card {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 30px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card h2 {
  margin-top: 0;
  margin-bottom: 15px;
  color: #333;
  font-size: 24px;
}

.news {
  background-color: #f9f9f9;
  padding: 40px 0;
  margin-top: 0;
}
</style>