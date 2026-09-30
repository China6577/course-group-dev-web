import axios from 'axios';

// 创建axios实例
const api = axios.create({
    baseURL: '/api',
    timeout: 10000,
});

// 通用请求处理函数
const requestHandler = (requestPromise, errorMsg) => {
    return requestPromise
        .then(response => response.data)
        .catch(error => {
            console.error(errorMsg, error);
            throw error; // 抛出错误，让调用方可以继续捕获
        });
};

// 封装后的API接口
export default {
    // 组织结构
    getOrganization() {
        return requestHandler(api.get('/members/'), '获取组织结构数据失败:');
    },

    // 研究方向
    getResearchDirections() {
        return requestHandler(api.get('/research-areas/'), '获取研究方向数据失败:');
    },

    // 论文发表
    getPublications() {
        return requestHandler(api.get('/publications/'), '获取论文发表数据失败:');
    },

    // 新闻列表
    getNews() {
        return requestHandler(api.get('/news/'), '获取新闻列表数据失败:');
    },

    // 合作伙伴
    getPartners() {
        return requestHandler(api.get('/partners/'), '获取合作伙伴数据失败:');
    },
};