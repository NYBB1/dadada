#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class examresults(BaseModel):
    __doc__ = u'''examresults'''
    __tablename__ = 'examresults'



    __authTables__={'studentid':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    studentid=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    timeofenrollment=models.DateField   (  null=True, unique=False, verbose_name='入学时间' )
    examtime=models.DateField   (  null=True, unique=False, verbose_name='考试时间' )
    gender=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    age=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年龄' )
    politicalachievements=models.FloatField   (  null=True, unique=False, verbose_name='政治成绩' )
    chinesescores=models.FloatField   (  null=True, unique=False, verbose_name='语文成绩' )
    mathematicsgrades=models.FloatField   (  null=True, unique=False, verbose_name='数学成绩' )
    foreignlanguagescore=models.FloatField   (  null=True, unique=False, verbose_name='外语成绩' )
    achievement=models.FloatField   (  null=True, unique=False, verbose_name='物理成绩' )
    chemistrygrades=models.FloatField   (  null=True, unique=False, verbose_name='化学成绩' )
    geographyscore=models.FloatField   (  null=True, unique=False, verbose_name='地理成绩' )
    historicalachievements=models.FloatField   (  null=True, unique=False, verbose_name='历史成绩' )
    totalscore=models.FloatField   (  null=True, unique=False, verbose_name='总成绩' )
    averagescore=models.FloatField   (  null=True, unique=False, verbose_name='平均成绩' )
    attendancerate=models.IntegerField  (  null=True, unique=False, verbose_name='出勤率' )
    homeworkcompletionrate=models.IntegerField  (  null=True, unique=False, verbose_name='作业完成度' )
    learningattitude=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学习态度' )
    familybackground=models.CharField ( max_length=255, null=True, unique=False, verbose_name='家庭背景' )
    teachingmethod=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教学方法' )
    parentseducationallevel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='父母教育水平' )
    extracurriculartutoringsituation=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课外辅导情况' )
    grade=models.CharField ( max_length=255, null=True, unique=False, verbose_name='等级' )
    '''
    studentid=VARCHAR
    timeofenrollment=Date
    examtime=Date
    gender=VARCHAR
    age=VARCHAR
    politicalachievements=Float
    chinesescores=Float
    mathematicsgrades=Float
    foreignlanguagescore=Float
    achievement=Float
    chemistrygrades=Float
    geographyscore=Float
    historicalachievements=Float
    totalscore=Float
    averagescore=Float
    attendancerate=Integer
    homeworkcompletionrate=Integer
    learningattitude=VARCHAR
    familybackground=VARCHAR
    teachingmethod=VARCHAR
    parentseducationallevel=VARCHAR
    extracurriculartutoringsituation=VARCHAR
    grade=VARCHAR
    '''
    class Meta:
        db_table = 'examresults'
        verbose_name = verbose_name_plural = '考试成绩'
class examresultsforecast1(BaseModel):
    __doc__ = u'''examresultsforecast1'''
    __tablename__ = 'examresultsforecast1'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    studentid=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    politicalachievements=models.FloatField   (  null=True, unique=False, verbose_name='政治成绩' )
    chinesescores=models.FloatField   (  null=True, unique=False, verbose_name='语文成绩' )
    mathematicsgrades=models.FloatField   (  null=True, unique=False, verbose_name='数学成绩' )
    foreignlanguagescore=models.FloatField   (  null=True, unique=False, verbose_name='外语成绩' )
    achievement=models.FloatField   (  null=True, unique=False, verbose_name='物理成绩' )
    chemistrygrades=models.FloatField   (  null=True, unique=False, verbose_name='化学成绩' )
    geographyscore=models.FloatField   (  null=True, unique=False, verbose_name='地理成绩' )
    historicalachievements=models.FloatField   (  null=True, unique=False, verbose_name='历史成绩' )
    averagescore=models.FloatField   (  null=True, unique=False, verbose_name='平均成绩' )
    '''
    studentid=VARCHAR
    politicalachievements=Float
    chinesescores=Float
    mathematicsgrades=Float
    foreignlanguagescore=Float
    achievement=Float
    chemistrygrades=Float
    geographyscore=Float
    historicalachievements=Float
    averagescore=Float
    '''
    class Meta:
        db_table = 'examresultsforecast1'
        verbose_name = verbose_name_plural = '平均成绩预测'
class examresultsforecast(BaseModel):
    __doc__ = u'''examresultsforecast'''
    __tablename__ = 'examresultsforecast'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    studentid=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    totalscore=models.FloatField   (  null=True, unique=False, verbose_name='总成绩' )
    averagescore=models.FloatField   (  null=True, unique=False, verbose_name='平均成绩' )
    attendancerate=models.IntegerField  (  null=True, unique=False, verbose_name='出勤率' )
    homeworkcompletionrate=models.IntegerField  (  null=True, unique=False, verbose_name='作业完成度' )
    learningattitude=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学习态度' )
    grade=models.CharField ( max_length=255, null=True, unique=False, verbose_name='等级' )
    '''
    studentid=VARCHAR
    totalscore=Float
    averagescore=Float
    attendancerate=Integer
    homeworkcompletionrate=Integer
    learningattitude=VARCHAR
    grade=VARCHAR
    '''
    class Meta:
        db_table = 'examresultsforecast'
        verbose_name = verbose_name_plural = '等级预测'
class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='studentid'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='studentid'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    studentid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='学号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xueshengxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学生姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    '''
    studentid=VARCHAR
    mima=VARCHAR
    xueshengxingming=VARCHAR
    touxiang=Text
    xingbie=VARCHAR
    shoujihaoma=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
