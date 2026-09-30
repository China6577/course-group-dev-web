<template>
  <div class="contact">
    <!-- 页面头部 -->
    <div class="page-header">
      <h1>加入我们</h1>
      <p>期待优秀的您加入我们的研究团队</p>
    </div>

    <div class="container">
      <div class="contact-content">
        <div class="contact-info card">
          <h2>联系信息</h2>
          <p>我们期待优秀的新成员加入我们团队！现面向国内外招收研究生（博士生、硕士生），并长期招聘研究助理！</p>
          <ul class="info-list">
            <li>
              <span class="info-label">地址：</span>
              <span class="info-value">联系地址待配置</span>
            </li>
            <li>
              <span class="info-label">邮箱：</span>
              <span class="info-value">contact@example.com</span>
            </li>
          </ul>
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

.contact {
  padding-bottom: 60px;
}

.contact-content {
  margin-top: 40px;
  display: flex;
  justify-content: center;
}

.contact-info {
  width: 100%;
  max-width: 800px;
}

.contact-info h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.contact-info > p {
  font-size: 1.15rem;
  line-height: 1.8;
  margin-bottom: 30px;
  color: #333;
}

.info-list {
  list-style: none;
  padding: 0;
}

.info-list li {
  margin-bottom: 25px;
  display: flex;
  flex-direction: column;
}

.info-label {
  font-weight: bold;
  color: #3498db;
  margin-bottom: 8px;
  font-size: 1.3rem;
}

.info-value {
  color: #555;
  font-size: 1.15rem;
  line-height: 1.6;
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

  .contact-content {
    padding: 0 20px;
  }
}
</style>