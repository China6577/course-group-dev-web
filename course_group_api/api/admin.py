from django.contrib import admin
from .models import ResearchArea, Member, Publication, Partner

# 站点头部
admin.site.site_header = '课题组后台管理系统'
# 管理站点标题
admin.site.site_title = '课题组后台管理系统'


@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):
    """研究方向管理"""
    list_display = ('name', 'order')
    search_fields = ('name', 'description', 'details')
    list_filter = ('order',)
    ordering = ('order', 'id')
    list_editable = ('order',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """团队成员管理"""
    list_display = ('name', 'role', 'title', 'is_leader', 'order')
    search_fields = ('name', 'specialty', 'bio')
    list_filter = ('role', 'is_leader')
    ordering = ('order', 'id')
    list_editable = ('order', 'is_leader')
    # 优化表单显示
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'phone', 'role', 'title', 'office', 'is_leader')
        }),
        ('详细信息', {
            'fields': ('specialty', 'email', 'homepage', 'avatar')
        }),
        ('排序', {
            'fields': ('order',)
        }),
        ('毕业信息', {
            'fields': ('research_result', 'graduation_destination')
        })
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """合作伙伴管理"""
    list_display = ('name', 'order')
    search_fields = ('name', 'description')
    list_filter = ('order',)
    ordering = ('order', 'id')
    list_editable = ('order',)
    # 优化表单显示
    fieldsets = (
        ('基本信息', {
            'fields': ('name',)
        }),
        ('详细信息', {
            'fields': ('description', 'website')
        }),
        ('排序', {
            'fields': ('order',)
        }),
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    """发表论文管理"""
    list_display = ('title', 'type', 'year', 'venue', 'citation_count')
    search_fields = ('title', 'authors', 'venue', 'abstract')
    list_filter = ('type', 'year')
    ordering = ('-year', 'title')
    date_hierarchy = None  # 不使用日期层次结构
    list_editable = ('year', 'venue')
    # 优化表单显示
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'authors', 'type')
        }),
        ('出版信息', {
            'fields': ('venue', 'year', 'abstract', 'bibtex_text')
        }),
        ('链接和引用', {
            'fields': ('paper_url', 'citation_count')
        }),
        ('排序权重', {
            'fields': ('order',)
        })
    )
