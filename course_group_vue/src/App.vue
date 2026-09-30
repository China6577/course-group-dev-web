<script setup>
import {RouterView} from 'vue-router'
import Header from './components/common/Header.vue'
import Footer from './components/common/Footer.vue'
</script>

<template>
  <Header/>

  <main class="main">
    <RouterView/>
  </main>

  <Footer/>
</template>

<style>
/* 全局样式重置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
  'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
  sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #f9f9f9;
  color: #333;
  line-height: 1.6;
}

/* 主内容区域样式 */
.main {
  min-height: 80vh;
  padding: 0;
  margin: 0;
}

/* 容器样式 */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* 标题通用样式 */
h1, h2, h3, h4, h5, h6 {
  color: #2c3e50;
  font-weight: 600;
  line-height: 1.3;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

h2 {
  font-size: 2rem;
  margin-bottom: 0.8rem;
  position: relative;
  padding-bottom: 10px;
}

h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 3px;
  background-color: #667eea;
  border-radius: 2px;
}

h3 {
  font-size: 1.5rem;
  margin-bottom: 0.6rem;
}

/* 段落样式 */
p {
  margin-bottom: 1rem;
  font-size: 1rem;
}

/* 链接通用样式 */
a {
  color: #667eea;
  text-decoration: none;
  transition: all 0.3s ease;
}

a:hover {
  color: #764ba2;
}

/* 卡片阴影效果 */
.card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
}

/* 按钮样式 */
.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
}

.btn:hover {
  background-color: #764ba2;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(65, 66, 72, 0.3);
}

.btn-outline {
  background-color: transparent;
  border: 2px solid #667eea;
  color: #667eea;
}

.btn-outline:hover {
  background-color: #667eea;
  color: white;
}

/* 响应式设计 */
@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  h2 {
    font-size: 1.6rem;
  }

  h3 {
    font-size: 1.3rem;
  }

  .main {
    padding: 0;
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 1.8rem;
  }

  h2 {
    font-size: 1.4rem;
  }

  h3 {
    font-size: 1.2rem;
  }
}
</style>