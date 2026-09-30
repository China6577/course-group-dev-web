const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    // 发环境专属，上线无用且易误判
    devServer: {
        port: 8080,
        proxy: {
            '/api': {
                target: process.env.COURSE_GROUP_API_TARGET || 'http://127.0.0.1:8000',
                changeOrigin: true,
            }
        }
    },
    // 默认适配低配手机 但会减慢构建时间
    transpileDependencies: true,
    lintOnSave: false
})
