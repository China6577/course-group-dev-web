<template>
  <footer class="main-footer">
    <div class="container footer-container">
      <!-- 联系信息 -->
      <div class="footer-section contact-section">
        <h3 class="section-title">加入我们</h3>
        <div class="contact-info">
          <p class="contact-item">
            <span class="icon">🏛️</span>
            <span>西交利物浦大学·文化智能技术创新与应用实验室</span>
          </p>
          <p class="contact-item">
            <span class="icon">📍</span>
            <span>联系地址待配置</span>
          </p>
          <p class="contact-item">
            <span class="icon">✉️</span>
            <span>contact@example.com</span>
          </p>
        </div>
      </div>

      <!-- 导航链接 -->
      <div class="footer-section links-section">
        <h3 class="section-title">快速链接</h3>
        <ul class="footer-links">
          <li>
            <router-link to="/" class="footer-link">关于我们</router-link>
          </li>
          <li>
            <router-link to="/research" class="footer-link">研究领域</router-link>
          </li>
          <li>
            <router-link to="/members" class="footer-link">研究团队</router-link>
          </li>
          <li>
            <router-link to="/publications" class="footer-link">学术成果</router-link>
          </li>
          <li>
            <router-link to="/partners" class="footer-link">合作伙伴</router-link>
          </li>
          <li>
            <router-link to="/contact" class="footer-link">加入我们</router-link>
          </li>
        </ul>
      </div>

      <!-- 社交媒体 -->
      <div class="footer-section social-section">
        <h3 class="section-title">关注我们</h3>
        <div class="social-links">
          <a href="#" class="social-link" aria-label="微信">
            <span class="social-icon">💬</span>
          </a>
          <a href="#" class="social-link" aria-label="微博">
            <span class="social-icon">🔖</span>
          </a>
          <a href="#" class="social-link" aria-label="GitHub">
            <span class="social-icon">💻</span>
          </a>
          <a href="#" class="social-link" aria-label="知乎">
            <span class="social-icon">❓</span>
          </a>
        </div>
        <p class="copyright">© 2026 文化智能技术创新与应用实验室 版权所有</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
defineOptions({
  name: 'FooterComponent',
})
</script>

<style scoped>
.main-footer {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 40px 0 20px;
  margin-top: 0;
}

.footer-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-section {
  display: flex;
  flex-direction: column;
}

.section-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #34495e;
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 50px;
  height: 2px;
  background-color: #667eea;
}

/* 联系信息样式 */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.contact-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
}

.contact-item .icon {
  font-size: 1.2rem;
  flex-shrink: 0;
  margin-top: 2px;
}

/* 链接样式 */
.footer-links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 10px 20px;
}

.footer-link {
  color: #bdc3c7;
  text-decoration: none;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  padding: 5px 0;
  display: inline-block;
}

.footer-link:hover {
  color: #667eea;
  transform: translateX(5px);
}

/* 社交媒体样式 */
.social-links {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: #34495e;
  border-radius: 50%;
  color: #ecf0f1;
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-link:hover {
  background-color: #667eea;
  transform: translateY(-3px);
}

.social-icon {
  font-size: 1.2rem;
}

.copyright {
  font-size: 0.85rem;
  color: #95a5a6;
  margin-top: auto;
  padding-top: 15px;
  text-align: center;
  border-top: 1px solid #34495e;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .footer-container {
    grid-template-columns: 1fr;
    gap: 40px;
    padding: 0 15px;
  }

  .main-footer {
    padding: 30px 0 15px;
  }

  .section-title {
    font-size: 1.1rem;
    margin-bottom: 15px;
  }

  .footer-links {
    grid-template-columns: 1fr 1fr;
    gap: 8px 15px;
  }

  .social-links {
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .footer-container {
    gap: 30px;
  }

  .contact-item {
    font-size: 0.9rem;
  }

  .footer-links {
    grid-template-columns: 1fr;
  }

  .social-link {
    width: 35px;
    height: 35px;
  }

  .social-icon {
    font-size: 1rem;
  }
}
</style>