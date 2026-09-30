from django.db import models


class ResearchArea(models.Model):
    """研究领域"""
    name = models.CharField(max_length=100, verbose_name='研究领域名称')
    description = models.TextField(verbose_name='简短描述')
    details = models.TextField(blank=True, null=True, verbose_name='详细介绍')
    order = models.IntegerField(default=0, help_text='排序权重', verbose_name='排序')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'id']
        verbose_name = '研究领域'
        verbose_name_plural = '研究领域'


class Member(models.Model):
    """团队成员"""
    ROLE_CHOICES = (
        ('head', '系主任'),
        ('professor', '教授'),
        ('associate_professor', '副教授'),
        ('lecturer', '讲师'),
        ('postdoctoral', '博士后'),
        ('phd', '博士研究生'),
        ('master', '硕士研究生'),
        ('undergraduate', '本科生'),
        ('research_assistant', '研究助理'),
        ('graduate', '毕业生'),
        ('other', '其他'),
    )

    name = models.CharField(max_length=50, verbose_name='姓名')
    phone = models.CharField(max_length=20, verbose_name='电话号码', blank=True, null=True,
                             help_text='请填写手机号或固定电话')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='职位')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='头衔')
    specialty = models.CharField(max_length=200, blank=True, null=True, verbose_name='研究领域')
    email = models.EmailField(blank=True, null=True, verbose_name='电子邮箱')
    avatar = models.ImageField(verbose_name='用户头像', upload_to='avatars/', blank=True, null=True)
    is_leader = models.BooleanField(default=False, help_text='是否为课题组负责人', verbose_name='是否为负责人')
    order = models.IntegerField(default=0, help_text='排序权重', verbose_name='排序')
    office = models.CharField(max_length=50, verbose_name='办公室', default="暂无办公室")
    research_result = models.CharField(max_length=50, verbose_name='研究成果', blank=True, null=True)
    graduation_destination = models.CharField(max_length=50, verbose_name='毕业去向', blank=True, null=True)
    homepage = models.URLField(blank=True, null=True, verbose_name='个人主页地址')

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"

    class Meta:
        ordering = ['order', 'id']
        verbose_name = '团队成员'
        verbose_name_plural = '团队成员'


class Publication(models.Model):
    """发表论文"""
    TYPE_CHOICES = (
        ('conference', '会议论文'),
        ('journal', '期刊论文'),
        ('other', '其他'),
    )

    title = models.CharField(max_length=255, verbose_name='论文标题', unique=True)
    authors = models.CharField(max_length=255, help_text='作者列表，逗号分隔', verbose_name='作者')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='类型')
    venue = models.CharField(max_length=200, blank=True, null=True, help_text='会议或期刊名称', verbose_name='发表刊物')
    year = models.IntegerField(verbose_name='发表年份')
    abstract = models.TextField(blank=True, null=True, verbose_name='摘要')
    paper_url = models.URLField(blank=True, null=True, verbose_name='论文链接')
    bibtex_text = models.TextField(blank=True, null=True, verbose_name='BibTeX文本',
                                   help_text='粘贴BibTeX条目')
    citation_count = models.IntegerField(default=0, blank=True, null=True, verbose_name='引用次数')
    order = models.IntegerField(default=100, blank=True, null=True, verbose_name='排序权重', help_text='权重越小越靠前')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-year', 'order', 'title']
        verbose_name = '学术成果'
        verbose_name_plural = '学术成果'


class Partner(models.Model):
    """合作伙伴"""
    name = models.CharField(max_length=100, verbose_name='名称')
    description = models.TextField(blank=True, null=True, verbose_name='描述')
    website = models.URLField(blank=True, null=True, verbose_name='网站链接')
    order = models.IntegerField(default=0, help_text='排序权重', verbose_name='排序')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'id']
        verbose_name = '合作伙伴'
        verbose_name_plural = '合作伙伴'
