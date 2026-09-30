<template>
  <header class="main-header">
    <div class="container header-container">
      <div class="logo-section">
        <router-link to="/" class="logo-link">
          <div class="logo">
            <span class="logo-icon">🏛️</span>
            <span class="logo-text">文化智能技术创新与应用实验室</span>
          </div>
        </router-link>
      </div>

      <!-- 桌面端导航 -->
      <nav class="main-nav desktop-nav">
        <ul class="nav-list">
          <li class="nav-item">
            <router-link to="/" class="nav-link" exact>关于我们</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/research" class="nav-link">研究领域</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/members" class="nav-link">研究团队</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/publications" class="nav-link">学术成果</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/partners" class="nav-link">合作伙伴</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/contact" class="nav-link">加入我们</router-link>
          </li>
        </ul>
      </nav>

      <!-- 移动端菜单按钮 -->
      <div class="mobile-menu-toggle">
        <button class="menu-button" @click="toggleMenu" aria-label="菜单">
          <span class="menu-icon"></span>
          <span class="menu-icon"></span>
          <span class="menu-icon"></span>
        </button>
      </div>
    </div>

    <!-- 移动端导航菜单 -->
    <nav class="mobile-nav" v-show="isMenuOpen">
      <ul class="mobile-nav-list">
        <li class="mobile-nav-item">
          <router-link to="/" class="mobile-nav-link" exact @click="closeMenu">关于我们</router-link>
        </li>
        <li class="mobile-nav-item">
          <router-link to="/research" class="mobile-nav-link" @click="closeMenu">研究领域</router-link>
        </li>
        <li class="mobile-nav-item">
          <router-link to="/members" class="mobile-nav-link" @click="closeMenu">研究团队</router-link>
        </li>
        <li class="mobile-nav-item">
          <router-link to="/publications" class="mobile-nav-link" @click="closeMenu">学术成果</router-link>
        </li>
        <li class="mobile-nav-item">
          <router-link to="/partners" class="mobile-nav-link" @click="closeMenu">合作伙伴</router-link>
        </li>
        <li class="mobile-nav-item">
          <router-link to="/contact" class="mobile-nav-link" @click="closeMenu">加入我们</router-link>
        </li>
      </ul>
    </nav>

    <!-- 背景遮罩 -->
    <div class="overlay" v-if="isMenuOpen" @click="closeMenu"></div>
  </header>
</template>

<script setup>
// 1. 保留导入语句
import {ref} from 'vue'

// 2. 声明组件名（替代原 export default 中的 name）
defineOptions({
  name: 'HeaderComponent',
})

// 3. 直接写原 setup 函数内的逻辑，无需包裹
const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}
</script>

<style scoped>
.main-header {
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
  margin-bottom: 0; /* 移除底部边距 */
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Logo 样式 */
.logo-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-icon {
  font-size: 2.2rem;
  margin-right: 12px;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: bold;
  color: #2c3e50;
}

/* 桌面端导航样式 */
.desktop-nav {
  display: block;
}

.nav-list {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-item {
  margin-left: 30px;
}

.nav-link {
  text-decoration: none;
  color: #555;
  font-size: 1rem;
  font-weight: 500;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: #667eea;
}

.nav-link.router-link-active {
  color: #667eea;
  font-weight: 600;
}

.nav-link.router-link-active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 3px;
  background-color: #667eea;
  border-radius: 2px;
}

/* 移动端菜单按钮 */
.mobile-menu-toggle {
  display: none;
}

.menu-button {
  background: none;
  border: none;
  padding: 10px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 24px;
}

.menu-icon {
  display: block;
  width: 100%;
  height: 3px;
  background-color: #555;
  border-radius: 2px;
  transition: all 0.3s ease;
}

.menu-button.open .menu-icon:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.menu-button.open .menu-icon:nth-child(2) {
  opacity: 0;
}

.menu-button.open .menu-icon:nth-child(3) {
  transform: rotate(-45deg) translate(6px, -6px);
}

/* 移动端导航样式 */
.mobile-nav {
  display: none;
  position: fixed;
  top: 0;
  right: 0;
  width: 80%;
  max-width: 300px;
  height: 100vh;
  background-color: white;
  box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
  z-index: 101;
  padding-top: 80px;
  transition: transform 0.3s ease;
}

.mobile-nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.mobile-nav-item {
  border-bottom: 1px solid #f0f0f0;
}

.mobile-nav-link {
  display: block;
  text-decoration: none;
  color: #555;
  font-size: 1.1rem;
  padding: 15px 20px;
  transition: all 0.3s ease;
}

.mobile-nav-link:hover,
.mobile-nav-link.router-link-active {
  background-color: #f8f9fa;
  color: #667eea;
  font-weight: 600;
}

/* 背景遮罩 */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 100;
  transition: opacity 0.3s ease;
}

/* 响应式设计 */
@media (max-width: 992px) {
  .nav-item {
    margin-left: 20px;
  }
}

@media (max-width: 768px) {
  .desktop-nav {
    display: none;
  }

  .mobile-menu-toggle {
    display: block;
  }

  .mobile-nav {
    display: block;
  }

  .logo-text {
    font-size: 1.2rem;
  }

  .logo-icon {
    font-size: 1.8rem;
    margin-right: 8px;
  }
}

@media (max-width: 480px) {
  .header-container {
    padding: 12px 15px;
  }

  .logo-text {
    font-size: 1.1rem;
  }

  .logo-icon {
    font-size: 1.6rem;
  }
}
</style>