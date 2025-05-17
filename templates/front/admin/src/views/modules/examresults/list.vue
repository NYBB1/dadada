<template>
	<div class="main-content" :style='{"padding":"60px 20px","margin":"0","fontSize":"15px"}'>
		<!-- 列表页 -->
		<template v-if="showFlag">
			<el-form class="center-form-pv" :style='{"margin":"0 0px 0px"}' :inline="true" :model="searchForm">
				<el-row :style='{"width":"100%","padding":"10px","flexWrap":"wrap","background":"none","display":"flex"}' >
					<div :style='{"margin":"0 10px 20px 0","display":"flex"}'>
						<label :style='{"border":"1px solid #CBCBCB","padding":"0 10px","margin":"0 10px 0 0","color":"#000","textAlign":"center","display":"inline-block","borderRadius":"10px","background":"#fff","width":"180px","lineHeight":"34px","fontSize":"inherit","fontWeight":"500","height":"34px"}' class="item-label">学号</label>
						<el-input v-model="searchForm.studentid" placeholder="学号" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<el-button class="search" type="success" @click="search()">
						<span class="icon iconfont icon-fangdajing07" :style='{"margin":"0 2px","fontSize":"16px","color":"#0F1330","height":"40px"}'></span>
						查询
					</el-button>
				</el-row>

				<el-row class="actions" :style='{"padding":"10px","margin":"0px 0","flexWrap":"wrap","background":"none","display":"flex"}'>
					<el-button class="add" v-if="isAuth('examresults','新增')" type="success" @click="addOrUpdateHandler()">
						<span class="icon iconfont icon-tianjia1" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","borderRadius":"5px","height":"34px"}'></span>
						添加
					</el-button>
					<el-button class="del" v-if="isAuth('examresults','删除')" :disabled="dataListSelections.length?false:true" type="danger" @click="deleteHandler()">
						<span class="icon iconfont icon-shanchu6" :style='{"margin":"0 2px","fontSize":"14px","color":"#6EADEF","height":"34px"}'></span>
						删除
					</el-button>

					<el-button class="btn18" v-if="isAuth('examresults','导入')" type="success" @click="importHandler()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						导入
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','上传模板')" type="success" @click="importClcik">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						上传模板
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','下载模板')" type="success" @click="download('upload/examresults_template.xlsx')">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						下载模板
					</el-button>

					<el-button class="btn18" v-if="isAuth('examresults','学生统计')" type="success" @click="chartDialog1()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						学生统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','成绩分析')" type="success" @click="chartDialog2()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						成绩分析
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','平均成绩统计')" type="success" @click="chartDialog3()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						平均成绩统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','学习态度统计')" type="success" @click="chartDialog4()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						学习态度统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','出勤率')" type="success" @click="chartDialog5()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						出勤率
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','作业完成度')" type="success" @click="chartDialog6()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						作业完成度
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','等级占比')" type="success" @click="chartDialog7()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						等级占比
					</el-button>
					<el-button class="btn18" v-if="isAuth('examresults','教学方法')" type="success" @click="chartDialog8()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"34px"}'></span>
						教学方法
					</el-button>
				</el-row>
			</el-form>
			<div :style='{"width":"100%","padding":"0 10px","fontSize":"14px","color":"#000"}'>
				<el-table class="tables"
					:stripe='true'
					:style='{"padding":"0","borderColor":"#eee","borderRadius":"20px 20px 0 0","borderWidth":"1px 0 0 1px","background":"#fff","width":"100%","fontSize":"inherit","borderStyle":"solid"}' 
					:border='true'
					v-if="isAuth('examresults','查看')"
					:data="dataList"
					v-loading="dataListLoading"
				@selection-change="selectionChangeHandler">
					<el-table-column :resizable='true' type="selection" align="center" width="50"></el-table-column>
					<el-table-column :resizable='true' :sortable='true' label="序号" type="index" width="50" />
					<el-table-column :resizable='true' :sortable='true'  
						prop="studentid"
						label="学号">
						<template slot-scope="scope">
							{{scope.row.studentid}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="timeofenrollment"
						label="入学时间">
						<template slot-scope="scope">
							{{scope.row.timeofenrollment}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="examtime"
						label="考试时间">
						<template slot-scope="scope">
							{{scope.row.examtime}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="gender"
						label="性别">
						<template slot-scope="scope">
							{{scope.row.gender}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="age"
						label="年龄">
						<template slot-scope="scope">
							{{scope.row.age}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="politicalachievements"
						label="政治成绩">
						<template slot-scope="scope">
							{{scope.row.politicalachievements}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="chinesescores"
						label="语文成绩">
						<template slot-scope="scope">
							{{scope.row.chinesescores}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="mathematicsgrades"
						label="数学成绩">
						<template slot-scope="scope">
							{{scope.row.mathematicsgrades}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="foreignlanguagescore"
						label="外语成绩">
						<template slot-scope="scope">
							{{scope.row.foreignlanguagescore}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="achievement"
						label="物理成绩">
						<template slot-scope="scope">
							{{scope.row.achievement}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="chemistrygrades"
						label="化学成绩">
						<template slot-scope="scope">
							{{scope.row.chemistrygrades}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="geographyscore"
						label="地理成绩">
						<template slot-scope="scope">
							{{scope.row.geographyscore}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="historicalachievements"
						label="历史成绩">
						<template slot-scope="scope">
							{{scope.row.historicalachievements}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="totalscore"
						label="总成绩">
						<template slot-scope="scope">
							{{scope.row.totalscore}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="averagescore"
						label="平均成绩">
						<template slot-scope="scope">
							{{scope.row.averagescore}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="attendancerate"
						label="出勤率">
						<template slot-scope="scope">
							{{scope.row.attendancerate}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="homeworkcompletionrate"
						label="作业完成度">
						<template slot-scope="scope">
							{{scope.row.homeworkcompletionrate}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="learningattitude"
						label="学习态度">
						<template slot-scope="scope">
							{{scope.row.learningattitude}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="familybackground"
						label="家庭背景">
						<template slot-scope="scope">
							{{scope.row.familybackground}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="teachingmethod"
						label="教学方法">
						<template slot-scope="scope">
							{{scope.row.teachingmethod}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="parentseducationallevel"
						label="父母教育水平">
						<template slot-scope="scope">
							{{scope.row.parentseducationallevel}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="extracurriculartutoringsituation"
						label="课外辅导情况">
						<template slot-scope="scope">
							{{scope.row.extracurriculartutoringsituation}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'  
						prop="grade"
						label="等级">
						<template slot-scope="scope">
							{{scope.row.grade}}
						</template>
					</el-table-column>
					<el-table-column width="300" label="操作">
						<template slot-scope="scope">
							<el-button class="view" v-if=" isAuth('examresults','查看')" type="success" @click="addOrUpdateHandler(scope.row.id,'info')">
								<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"40px"}'></span>
								查看
							</el-button>
							<el-button class="edit" v-if=" isAuth('examresults','修改') " type="success" @click="addOrUpdateHandler(scope.row.id)">
								<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"40px"}'></span>
								修改
							</el-button>




							<el-button class="del" v-if="isAuth('examresults','删除') " type="primary" @click="deleteHandler(scope.row.id )">
								<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"40px"}'></span>
								删除
							</el-button>
						</template>
					</el-table-column>
				</el-table>
			</div>
			<el-pagination
				@size-change="sizeChangeHandle"
				@current-change="currentChangeHandle"
				:current-page="pageIndex"
				background
				:page-sizes="[10, 50, 100, 200]"
				:page-size="pageSize"
				:layout="layouts.join()"
				:total="totalPage"
				prev-text="< "
				next-text="> "
				:hide-on-single-page="false"
				:style='{"border":" 0px solid #F1F1F1","padding":"0","margin":"20px auto 0","whiteSpace":"nowrap","color":"#000000","textAlign":"center","display":"flex","justifyContent":"space-between","borderRadius":"5px","background":"none","width":"750px","fontSize":"12","fontWeight":"400","height":"50px"}'
			></el-pagination>
		</template>
		
		<!-- 添加/修改页面  将父组件的search方法传递给子组件-->
		<add-or-update v-if="addOrUpdateFlag" :parent="this" ref="addOrUpdate"></add-or-update>



		<el-dialog title="导入" :visible.sync="importVisiable" width="50%">
			<el-form ref="form" :model="form" label-width="80px">
				<el-form-item class="upload" label="文件" prop="excelFile">
				  <excel-file-upload
				  tip="点击上传直接导入excel文件"
				  action="examresults/importExcel"
				  :limit="1"
				  :fileUrls="importUrl"
				  @change="importChange"
				  ></excel-file-upload>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button @click="importHandler()">关 闭</el-button>
			</span>
		</el-dialog>
		<el-dialog title="上传模板" :visible.sync="importVis" width="50%">
			<el-form ref="form" :model="importForm" label-width="80px">
				<el-form-item class="upload" label="文件" prop="excelFile">
					<el-upload class="upload-demo" drag :action="$base.url + 'file/upload?type=examresults_template'"
						:show-file-list="false" :on-success="importSuccess">
						<i class="el-icon-upload"></i>
						<div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
					</el-upload>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button @click="importVis=false">关 闭</el-button>
			</span>
		</el-dialog>

		<el-dialog
			:visible.sync="chartVisiable1"
			width="800">
			<div id="genderChart1" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog1">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			:visible.sync="chartVisiable2"
			width="800">
			<div id="studentidChart2" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog2">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			:visible.sync="chartVisiable3"
			width="800">
			<div id="averagescoreChart3" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog3">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			:visible.sync="chartVisiable4"
			width="800">
			<div id="learningattitudeChart4" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog4">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			:visible.sync="chartVisiable5"
			width="800">
			<div id="attendancerateChart5" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog5">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			:visible.sync="chartVisiable6"
			width="800">
			<div id="homeworkcompletionrateChart6" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog6">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			:visible.sync="chartVisiable7"
			width="800">
			<div id="gradeChart7" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog7">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			:visible.sync="chartVisiable8"
			width="800">
			<div id="teachingmethodChart8" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartDialog8">返回</el-button>
			</span>
		</el-dialog>

	</div>
</template>

<script>
	import * as echarts from 'echarts'
	import chinaJson from "@/components/echarts/china.json";
	import axios from 'axios';
	import AddOrUpdate from "./add-or-update";
	import {
		Loading
	} from 'element-ui';
	export default {
		data() {
			return {
				indexQueryCondition: '',
				searchForm: {
					key: ""
				},
				form:{},
				dataList: [],
				pageIndex: 1,
				pageSize: 10,
				totalPage: 0,
				dataListLoading: false,
				dataListSelections: [],
				showFlag: true,
				importVisiable: false,
				importVis: false,
				importForm: {},
				importUrl: '',
				chartVisiable1: false,
				line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#19406E","#507AFC","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"#333","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"showSymbol":true,"symbol":"emptyCircle","symbolSize":4},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"}},
				bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#6EADEF","#D6C1CA","#77A0CC","#6EADEF","#D6C1CA","#77A0CC","#6EADEF","#D6C1CA","#77A0CC"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"#333","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"barWidth":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"colorBy":"data","barCategoryGap":"20%"},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"center","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"base":{"animate":false,"interval":2000}},
				pie: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#6EADEF","#D6C1CA","#77A0CC","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"borderType":"solid","padding":[5,0,0,0],"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":[5,0,0,0],"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":0,"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#666","color":"inherit","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#666","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"top":"30%"}},
				funnel: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"borderType":"solid","padding":2,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"center","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#666","textShadowColor":"transparent","fontSize":14,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
				boardBase: {"funnelNum":10,"lineNum":10,"gaugeNum":8,"barNum":10,"pieNum":10},
				gauge: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"top":"top","left":"left","textStyle":{"fontSize":14,"lineHeight":24,"color":"#333","fontWeight":600}},"series":{"pointer":{"offsetCenter":[0,"10%"],"icon":"path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z","width":8,"length":"80%"},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"opacity":0.5,"shadowBlur":1,"shadowColor":"#000"},"roundCap":true},"anchor":{"show":true,"itemStyle":{"color":"inherit"},"size":18,"showAbove":true},"emphasis":{"disabled":false},"progress":{"show":true,"roundCap":true,"overlap":true},"splitNumber":25,"detail":{"formatter":"{value}","backgroundColor":"inherit","color":"#fff","borderRadius":3,"width":20,"fontSize":12,"height":10},"title":{"fontSize":14},"animation":true}},
				chartVisiable2: false,
				chartVisiable3: false,
				chartVisiable4: false,
				chartVisiable5: false,
				chartVisiable6: false,
				chartVisiable7: false,
				chartVisiable8: false,
				addOrUpdateFlag:false,
				layouts: ["total","prev","pager","next","sizes","jumper"],
			};
		},
		created() {
			this.init();
			this.getDataList();
			this.contentStyleChange();
		},
		mounted() {
		},
		filters: {
			htmlfilter: function (val) {
				return val.replace(/<[^>]*>/g).replace(/undefined/g,'');
			}
		},
		computed: {
			tablename(){
				return this.$storage.get('sessionTable')
			},
		},
		components: {
			AddOrUpdate,
		},
		methods: {
			contentStyleChange() {
				this.contentPageStyleChange()
			},
			// 分页
			contentPageStyleChange(){
				let arr = []

				// if(this.contents.pageTotal) arr.push('total')
				// if(this.contents.pageSizes) arr.push('sizes')
				// if(this.contents.pagePrevNext){
				//   arr.push('prev')
				//   if(this.contents.pagePager) arr.push('pager')
				//   arr.push('next')
				// }
				// if(this.contents.pageJumper) arr.push('jumper')
				// this.layouts = arr.join()
				// this.contents.pageEachNum = 10
			},


			// 统计接口
			chartDialog1() {
				this.chartVisiable1 = !this.chartVisiable1;
				this.$nextTick(()=>{
					var genderChart1 = echarts.init(document.getElementById("genderChart1"),'macarons');
					this.$http({
						url: "examresults/group/gender",
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.pieNum){
									break;
								}
								xAxis.push(res[i].gender);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].gender
								})
							}
							var option = {};
							let titleObj = this.pie.title
							titleObj.text = '学生统计'
							
							const legendObj = this.pie.legend
							let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
							tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
							
							let seriesObj = {
								type: 'pie',
								radius: '55%',
								center: ['50%', '60%'],
								data: pArray,
								emphasis: {
									itemStyle: {
										shadowBlur: 10,
										shadowOffsetX: 0,
										shadowColor: 'rgba(0, 0, 0, 0.5)'
									}
								}
							}
							seriesObj = Object.assign(seriesObj , this.pie.series)
							const gridObj = this.pie.grid
							option = {
								backgroundColor: this.pie.backgroundColor,
								color: this.pie.color,
								title: titleObj,
								legend: legendObj,
								grid: gridObj,
								tooltip: tooltipObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							genderChart1.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								genderChart1.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},

			// 统计接口
			chartDialog2() {
				this.chartVisiable2 = !this.chartVisiable2;
				this.$nextTick(()=>{

					var studentidChart2 = echarts.init(document.getElementById("studentidChart2"),'macarons');
					this.$http({
						url: `examresults/valueMul/studentid?yColumnNameMul=politicalachievements,chinesescores,mathematicsgrades,foreignlanguagescore,achievement,chemistrygrades,geographyscore,historicalachievements`,
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis1 = [];
							let yAxis1 = [];
							let pArray1 = []
							for(let i=0;i<res[0].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis1.push(res[0][i].studentid);
								yAxis1.push(parseFloat((res[0][i].total)));
								pArray1.push({
									value: parseFloat((res[0][i].total)),
									name: res[0][i].studentid
								})
							}
							let xAxis2 = [];
							let yAxis2 = [];
							let pArray2 = []
							for(let i=0;i<res[1].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis2.push(res[1][i].studentid);
								yAxis2.push(parseFloat((res[1][i].total)));
								pArray2.push({
									value: parseFloat((res[1][i].total)),
									name: res[1][i].studentid
								})
							}
							let xAxis3 = [];
							let yAxis3 = [];
							let pArray3 = []
							for(let i=0;i<res[2].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis3.push(res[2][i].studentid);
								yAxis3.push(parseFloat((res[2][i].total)));
								pArray3.push({
									value: parseFloat((res[2][i].total)),
									name: res[2][i].studentid
								})
							}
							let xAxis4 = [];
							let yAxis4 = [];
							let pArray4 = []
							for(let i=0;i<res[3].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis4.push(res[3][i].studentid);
								yAxis4.push(parseFloat((res[3][i].total)));
								pArray4.push({
									value: parseFloat((res[3][i].total)),
									name: res[3][i].studentid
								})
							}
							let xAxis5 = [];
							let yAxis5 = [];
							let pArray5 = []
							for(let i=0;i<res[4].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis5.push(res[4][i].studentid);
								yAxis5.push(parseFloat((res[4][i].total)));
								pArray5.push({
									value: parseFloat((res[4][i].total)),
									name: res[4][i].studentid
								})
							}
							let xAxis6 = [];
							let yAxis6 = [];
							let pArray6 = []
							for(let i=0;i<res[5].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis6.push(res[5][i].studentid);
								yAxis6.push(parseFloat((res[5][i].total)));
								pArray6.push({
									value: parseFloat((res[5][i].total)),
									name: res[5][i].studentid
								})
							}
							let xAxis7 = [];
							let yAxis7 = [];
							let pArray7 = []
							for(let i=0;i<res[6].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis7.push(res[6][i].studentid);
								yAxis7.push(parseFloat((res[6][i].total)));
								pArray7.push({
									value: parseFloat((res[6][i].total)),
									name: res[6][i].studentid
								})
							}
							let xAxis8 = [];
							let yAxis8 = [];
							let pArray8 = []
							for(let i=0;i<res[7].length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis8.push(res[7][i].studentid);
								yAxis8.push(parseFloat((res[7][i].total)));
								pArray8.push({
									value: parseFloat((res[7][i].total)),
									name: res[7][i].studentid
								})
							}
							var option = {};
							let titleObj = this.line.title
							titleObj.text = '成绩分析'
							
							const legendObj = this.line.legend
							legendObj.data = [
								'政治'.split('/').length>1?'政治'.split('/')[0]:'政治',
								'语文'.split('/').length>1?'语文'.split('/')[0]:'语文',
								'数学'.split('/').length>1?'数学'.split('/')[0]:'数学',
								'外语'.split('/').length>1?'外语'.split('/')[0]:'外语',
								'物理'.split('/').length>1?'物理'.split('/')[0]:'物理',
								'化学'.split('/').length>1?'化学'.split('/')[0]:'化学',
								'地理'.split('/').length>1?'地理'.split('/')[0]:'地理',
								'历史'.split('/').length>1?'历史'.split('/')[0]:'历史',
							]
				
							let xAxisObj = this.line.xAxis
							xAxisObj.type = 'category'
							xAxisObj.boundaryGap = false
							xAxisObj.data = xAxis1
							
							let yAxisObj = this.line.yAxis
							yAxisObj.type = 'value'
							
							let seriesObj = [
								{
									data: yAxis1,
									type: '政治'.split('/').length>1?'政治'.split('/')[1]:'line',
									name: '政治'.split('/').length>1?'政治'.split('/')[0]:'政治',
								},
								{
									data: yAxis2,
									type: '语文'.split('/').length>1?'语文'.split('/')[1]:'line',
									name: '语文'.split('/').length>1?'语文'.split('/')[0]:'语文',
								},
								{
									data: yAxis3,
									type: '数学'.split('/').length>1?'数学'.split('/')[1]:'line',
									name: '数学'.split('/').length>1?'数学'.split('/')[0]:'数学',
								},
								{
									data: yAxis4,
									type: '外语'.split('/').length>1?'外语'.split('/')[1]:'line',
									name: '外语'.split('/').length>1?'外语'.split('/')[0]:'外语',
								},
								{
									data: yAxis5,
									type: '物理'.split('/').length>1?'物理'.split('/')[1]:'line',
									name: '物理'.split('/').length>1?'物理'.split('/')[0]:'物理',
								},
								{
									data: yAxis6,
									type: '化学'.split('/').length>1?'化学'.split('/')[1]:'line',
									name: '化学'.split('/').length>1?'化学'.split('/')[0]:'化学',
								},
								{
									data: yAxis7,
									type: '地理'.split('/').length>1?'地理'.split('/')[1]:'line',
									name: '地理'.split('/').length>1?'地理'.split('/')[0]:'地理',
								},
								{
									data: yAxis8,
									type: '历史'.split('/').length>1?'历史'.split('/')[1]:'line',
									name: '历史'.split('/').length>1?'历史'.split('/')[0]:'历史',
								},
							]
							for(let i=0;i<seriesObj.length;i++){
								seriesObj[i] = Object.assign(seriesObj[i] , this.line.series)
							}
							
							let tooltipObj = {trigger: 'axis'}
							tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
							const gridObj = this.line.grid
							option = {
								backgroundColor: this.line.backgroundColor,
								color: this.line.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: seriesObj,
								grid: gridObj
							};
							// 使用刚指定的配置项和数据显示图表。
							studentidChart2.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								studentidChart2.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},

			// 统计接口
			chartDialog3() {
				this.chartVisiable3 = !this.chartVisiable3;
				this.$nextTick(()=>{

					var averagescoreChart3 = echarts.init(document.getElementById("averagescoreChart3"),'macarons');
					this.$http({
						url: "examresults/sectionStat/averagescore",
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.barNum){
									break;
								}
								xAxis.push(res[i].averagescore);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].averagescore
								})
							}
							var option = {};
							let titleObj = this.bar.title
							titleObj.text = '平均成绩统计'
							
							const legendObj = this.bar.legend
							let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
							tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
				
							let xAxisObj = this.bar.xAxis
							xAxisObj.type = 'category'
							xAxisObj.data = xAxis
							
							let yAxisObj = this.bar.yAxis
							yAxisObj.type = 'value'
				
							let seriesObj = {
								data: yAxis,
								type: 'bar',
							}
							seriesObj = Object.assign(seriesObj , this.bar.series)
							const gridObj = this.bar.grid
							option = {
								backgroundColor: this.bar.backgroundColor,
								color: this.bar.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj],
								grid: gridObj
							};
							// 使用刚指定的配置项和数据显示图表。
							averagescoreChart3.setOption(option);
							//根据窗口的大小变动图表
							window.onresize = function() {
								averagescoreChart3.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},

			// 统计接口
			chartDialog4() {
				this.chartVisiable4 = !this.chartVisiable4;
				this.$nextTick(()=>{

					var learningattitudeChart4 = echarts.init(document.getElementById("learningattitudeChart4"),'macarons');
					this.$http({
						url: "examresults/group/learningattitude",
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.barNum){
									break;
								}
								xAxis.push(res[i].learningattitude);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].learningattitude
								})
							}
							var option = {};
							let titleObj = this.bar.title
							titleObj.text = '学习态度统计'
							
							const legendObj = this.bar.legend
							let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
							tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
				
							let xAxisObj = this.bar.xAxis
							xAxisObj.type = 'value'
							
							let yAxisObj = this.bar.yAxis
							yAxisObj.type = 'category'
							yAxisObj.data = xAxis
				
							let seriesObj = {
								data: yAxis,
								type: 'bar',
							}
							seriesObj = Object.assign(seriesObj , this.bar.series)
							const gridObj = this.bar.grid

							option = {
								backgroundColor: this.bar.backgroundColor,
								color: this.bar.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj],
								grid: gridObj
							};
							// 使用刚指定的配置项和数据显示图表。
							learningattitudeChart4.setOption(option);
							//根据窗口的大小变动图表
							window.onresize = function() {
								learningattitudeChart4.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			// 统计接口
			chartDialog5() {
				this.chartVisiable5 = !this.chartVisiable5;
				this.$nextTick(()=>{

					var attendancerateChart5 = echarts.init(document.getElementById("attendancerateChart5"),'macarons');
					this.$http({
						url: `examresults/value/studentid/attendancerate`,
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.lineNum){
									break;
								}
								xAxis.push(res[i].studentid);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].studentid
								})
							}
							var option = {};
							let titleObj = this.line.title
							titleObj.text = '出勤率'
							
							const legendObj = this.line.legend
							let tooltipObj = { trigger: 'item',formatter: '{b} : {c}'}
							tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
							
							let xAxisObj = this.line.xAxis
							xAxisObj.type = 'category'
							xAxisObj.boundaryGap = false
							xAxisObj.data = xAxis
							
							let yAxisObj = this.line.yAxis
							yAxisObj.type = 'value'
							
							let seriesObj = {
								data: yAxis,
								type: 'line',
							}
							seriesObj = Object.assign(seriesObj , this.line.series)
							const gridObj = this.line.grid
							option = {
								backgroundColor: this.line.backgroundColor,
								color: this.line.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj],
								grid: gridObj
							};
							// 使用刚指定的配置项和数据显示图表。
							attendancerateChart5.setOption(option);
							//根据窗口的大小变动图表
							window.onresize = function() {
								attendancerateChart5.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			// 统计接口
			chartDialog6() {
				this.chartVisiable6 = !this.chartVisiable6;
				this.$nextTick(()=>{

					var homeworkcompletionrateChart6 = echarts.init(document.getElementById("homeworkcompletionrateChart6"),'macarons');
					this.$http({
						url: `examresults/value/studentid/homeworkcompletionrate`,
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.funnelNum){
									break;
								}
								xAxis.push(res[i].studentid);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].studentid
								})
							}
							var option = {};
							let titleObj = this.funnel.title
							titleObj.text = '作业完成度'
							
							let legendObj = {
								data: xAxis,
							}
							legendObj = Object.assign(legendObj , this.funnel.legend)
							let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
							tooltipObj = Object.assign(tooltipObj , this.funnel.tooltip?this.funnel.tooltip:{})
							let seriesObj = {
								name: '作业完成度',
								data: pArray,
								type: 'funnel',
								left: '10%',
								top: 60,
								bottom: 60,
								width: '80%',
								minSize: '0%',
								maxSize: '100%',
							}
							seriesObj = Object.assign(seriesObj , this.funnel.series)
							const gridObj = this.funnel.grid
							option = {
								backgroundColor: this.funnel.backgroundColor,
								color: this.funnel.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								series: seriesObj,
								grid: gridObj
							}
							// 使用刚指定的配置项和数据显示图表。
							homeworkcompletionrateChart6.setOption(option);
							//根据窗口的大小变动图表
							window.onresize = function() {
								homeworkcompletionrateChart6.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			// 统计接口
			chartDialog7() {
				this.chartVisiable7 = !this.chartVisiable7;
				this.$nextTick(()=>{

					var gradeChart7 = echarts.init(document.getElementById("gradeChart7"),'macarons');
					this.$http({
						url: "examresults/group/grade",
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								if(this.boardBase&&i==this.boardBase.pieNum){
									break;
								}
								xAxis.push(res[i].grade);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].grade
								})
							}
							var option = {};
							let titleObj = this.pie.title
							titleObj.text = '等级占比'
							
							const legendObj = this.pie.legend
							let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
							tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
							
							let seriesObj = {
								type: 'pie',
								radius: ['25%', '55%'],
								roseType: 'area',
								center: ['50%', '60%'],
								data: pArray,
								emphasis: {
									itemStyle: {
										shadowBlur: 10,
										shadowOffsetX: 0,
										shadowColor: 'rgba(0, 0, 0, 0.5)'
									}
								}
							}
							seriesObj = Object.assign(seriesObj , this.pie.series)
							const gridObj = this.pie.grid
							option = {
								backgroundColor: this.pie.backgroundColor,
								color: this.pie.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								series: [seriesObj],
								grid: gridObj
							};
							// 使用刚指定的配置项和数据显示图表。
							gradeChart7.setOption(option);
							//根据窗口的大小变动图表
							window.onresize = function() {
								gradeChart7.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			// 统计接口
			chartDialog8() {
				this.chartVisiable8 = !this.chartVisiable8;
				this.$nextTick(()=>{

					var teachingmethodChart8 = echarts.init(document.getElementById("teachingmethodChart8"),'macarons');
					this.$http({
						url: "examresults/group/teachingmethod",
						method: "get",
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
							let xAxis = [];
							let yAxis = [];
							let pArray = []
							for(let i=0;i<res.length;i++){
								xAxis.push(res[i].teachingmethod);
								yAxis.push(parseFloat((res[i].total)));
								pArray.push({
									value: parseFloat((res[i].total)),
									name: res[i].teachingmethod
								})
							}
							var option = {};
							// 使用刚指定的配置项和数据显示图表。
							teachingmethodChart8.setOption(option);
							//根据窗口的大小变动图表
							window.onresize = function() {
								teachingmethodChart8.resize();
							};
						}else{
							this.$message({
								message: data.msg,
								type: "warning",
								duration: 1500,
							})
						}
					});
				})
			},
			init () {
			},
			search() {
				this.pageIndex = 1;
				this.getDataList();
			},

			// 获取数据列表
			getDataList() {
				this.dataListLoading = true;
				let params = {
					page: this.pageIndex,
					limit: this.pageSize,
					sort: 'id',
					order: 'desc',
				}
 				if(this.searchForm.studentid!='' && this.searchForm.studentid!=undefined){
					params['studentid'] = '%' + this.searchForm.studentid + '%'
				}
				let user = JSON.parse(this.$storage.getObj('userForm'))
				this.$http({
					url: "examresults/page",
					method: "get",
					params: params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.dataList = data.data.list;
						this.totalPage = data.data.total;
					} else {
						this.dataList = [];
						this.totalPage = 0;
					}
					this.dataListLoading = false;
				});
			},
			// 每页数
			sizeChangeHandle(val) {
				this.pageSize = val;
				this.pageIndex = 1;
				this.getDataList();
			},
			// 当前页
			currentChangeHandle(val) {
				this.pageIndex = val;
				this.getDataList();
			},
			// 多选
			selectionChangeHandler(val) {
				this.dataListSelections = val;
			},
			// 添加/修改
			addOrUpdateHandler(id,type) {
				this.showFlag = false;
				this.addOrUpdateFlag = true;
				this.crossAddOrUpdateFlag = false;
				if(type!='info'&&type!='msg'){
					type = 'else';
				}
				this.$nextTick(() => {
					this.$refs.addOrUpdate.init(id,type);
				});
			},
			importChange(){
				this.importHandler()
				this.getDataList()
			},
			importClcik() {
				this.importVis = true
			},
			importSuccess(e) {
				if(e.code==0){
					this.$message.success('上传成功');
					this.importVis = false
					
				}
			},
			importHandler() {
				this.importUrl = ''
				this.importVisiable = !this.importVisiable;
			},
			// 下载
			download(file){
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.$base.url + 'file/download?fileName=' + arr, {
					headers: {
						token: this.$storage.get('Token')
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$base.name).length>1 ? location.href.split(this.$base.name)[0] :'') + this.$base.name + '/file/download?fileName=' + arr, {
						headers: {
							token: this.$storage.get('Token')
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},
			// 删除
			async deleteHandler(id ) {
				var ids = id? [Number(id)]: this.dataListSelections.map(item => {
					return Number(item.id);
				});
				await this.$confirm(`确定进行[${id ? "删除" : "批量删除"}]操作?`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(async () => {
					await this.$http({
						url: "examresults/delete",
						method: "post",
						data: ids
					}).then(async ({ data }) => {
						if (data && data.code === 0) {
							this.$message({
								message: "操作成功",
								type: "success",
								duration: 1500,
								onClose: () => {
									this.search();
								}
							});
			
						} else {
							this.$message.error(data.msg);
						}
					});
				});
			},


		}

	};
</script>
<style lang="scss" scoped>
	
	.center-form-pv {
		.el-date-editor.el-input {
			width: auto;
		}
	}
	
	.el-input {
		width: auto;
	}
	
	// form
	.center-form-pv .el-input {
		width: 100%;
	}
	.center-form-pv .el-input /deep/ .el-input__inner {
		border: 1px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 12px;
		color: #000;
		background: #fff;
		width: 170px;
		font-size: 16px;
		height: 34px;
	}
	.center-form-pv .el-select {
		width: 100%;
	}
	.center-form-pv .el-select /deep/ .el-input__inner {
		border: 1px solid #ddd;
		border-radius: 0px;
		padding: 0 10px;
		color: #000;
		width: 170px;
		font-size: 16px;
		height: 34px;
	}
	.center-form-pv .el-date-editor {
		width: 100%;
	}
	
	.center-form-pv .el-date-editor /deep/ .el-input__inner {
		border: 1px solid #ddd;
		border-radius: 0px;
		padding: 0 10px 0 30px;
		color: #000;
		width: 170px;
		font-size: 16px;
		height: 34px;
	}
	
	.center-form-pv .search {
		border: 0;
		cursor: pointer;
		border-radius: 5px;
		padding: 0 10px;
		color: #0F1330;
		background: #AFD0F5;
		width: auto;
		font-size: 16px;
		height: 34px;
	}
	
	.center-form-pv .search:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .add {
		border: 0px solid #ddd;
		cursor: pointer;
		border-radius: 5px;
		padding: 0 10px;
		margin: 4px;
		color: #fff;
		background: #6EADEF;
		width: auto;
		font-size: inherit;
		height: 34px;
	}
	
	.center-form-pv .actions .add:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .del {
		border: 1px solid #6EADEF;
		cursor: pointer;
		border-radius: 5px;
		padding: 0 10px;
		margin: 4px;
		color: #6EADEF;
		background: #fff;
		width: auto;
		font-size: inherit;
		height: 34px;
	}
	
	.center-form-pv .actions .del:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .statis {
		border: 1px solid #6EADEF;
		cursor: pointer;
		border-radius: 5px;
		padding: 0 10px;
		margin: 4px;
		color:  #6EADEF;
		background: #fff;
		width: auto;
		font-size: inherit;
		height: 34px;
	}
	
	.center-form-pv .actions .statis:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .btn18 {
		border: 1px solid #6EADEF;
		cursor: pointer;
		border-radius: 5px;
		padding: 0 10px;
		margin: 4px;
		color:  #6EADEF;
		background: #fff;
		width: auto;
		font-size: inherit;
		height: 34px;
	}
	
	.center-form-pv .actions .btn18:hover {
		opacity: 0.8;
	}
	
	// table
	.el-table /deep/ .el-table__header-wrapper thead {
		width: 100%;
	}
	
	.el-table /deep/ .el-table__header-wrapper thead tr {
	}
	
	.el-table /deep/ .el-table__header-wrapper thead tr th {
		padding: 0 10px;
		background: #EEEEEE;
		border-color: #eee;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: left;
	}

	.el-table /deep/ .el-table__header-wrapper thead tr th .cell {
		padding: 0 0 0 0px;
		word-wrap: normal;
		color: #000000;
		white-space: normal;
		font-weight: 400;
		display: flex;
		vertical-align: middle;
		font-size: 14px;
		line-height: 24px;
		text-overflow: ellipsis;
		word-break: break-all;
		width: 100%;
		align-items: center;
		position: relative;
	}

	.el-table /deep/ .el-table__body-wrapper {
		position: relative;
	}
	.el-table /deep/ .el-table__body-wrapper tbody {
		width: 100%;
	}

	.el-table /deep/ .el-table__body-wrapper tbody tr {
		background: #fff;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
		padding:  0px;
		color: #9E9E9E;
		background: #fff;
		font-size: inherit;
		border-color: #eee;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: left;
	}
	
		.el-table /deep/ .el-table__body-wrapper tbody tr.el-table__row--striped td {
		background: #f8f8f8;
	}
		
	.el-table /deep/ .el-table__body-wrapper tbody tr:hover td {
		padding: 0;
		color: #333;
		background: #f0f0f0;
		border-color: #eee;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: left;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
		padding:  0px;
		color: #9E9E9E;
		background: #fff;
		font-size: inherit;
		border-color: #eee;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: left;
	}

	.el-table /deep/ .el-table__body-wrapper tbody tr td .cell {
		padding: 0 0 0 8px;
		overflow: hidden;
		color: #666;
		word-break: break-all;
		white-space: normal;
		line-height: 24px;
		text-overflow: ellipsis;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view {
		border: 1px solid #D8D8D8;
		cursor: pointer;
		border-radius: 2px;
		padding: 0 5px;
		margin: 0 5px 5px 0;
		color: #000000;
		background: none;
		font-weight: 400;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view:hover {
		opacity: 0.8;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add {
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add:hover {
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit {
		border: 1px solid #D8D8D8;
		cursor: pointer;
		border-radius: 2px;
		padding: 0 5px;
		margin: 0 5px 5px 0;
		color: #000000;
		background: none;
		font-weight: 400;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit:hover {
		opacity: 0.8;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del {
		border: 1px solid #D8D8D8;
		cursor: pointer;
		border-radius: 2px;
		padding: 0 5px;
		margin: 0 5px 5px 0;
		color: #000000;
		background: none;
		font-weight: 400;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del:hover {
		opacity: 0.8;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8 {
		border: 1px solid #D8D8D8;
		cursor: pointer;
		border-radius: 2px;
		padding: 0 5px;
		margin: 0 5px 5px 0;
		color: #000000;
		background: none;
		font-weight: 400;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8:hover {
		opacity: 0.8;
	}
	
	// pagination
	.main-content .el-pagination /deep/ .el-pagination__total {
		margin: 0 10px 0 0;
		color: #666;
		font-weight: 400;
		vertical-align: top;
		font-size: inherit;
		line-height: 42px;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .btn-prev {
		border: none;
		border-radius: 100%;
		padding: 0;
		margin: 0 5px;
		color: #fff;
		background: #0F1330;
		display: block;
		vertical-align: top;
		width: 42px;
		font-size: 16px;
		line-height: auto;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .btn-next {
		border: none;
		padding: 0;
		margin: 0 5px;
		color: #fff;
		display: block;
		vertical-align: top;
		font-size: 16px;
		line-height: auto;
		border-radius: 50%;
		background: #0F1330;
		width: 42px;
		min-width: 35px;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .btn-prev:disabled {
		border: none;
		cursor: not-allowed;
		padding: 0;
		margin: 0 5px;
		color: #C0C4CC;
		display: block;
		vertical-align: top;
		font-size: 16px;
		line-height: auto;
		border-radius: 50%;
		background: #0F1330;
		width: 42px;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .btn-next:disabled {
		border: none;
		cursor: not-allowed;
		padding: 0;
		margin: 0 5px;
		color: #C0C4CC;
		display: block;
		vertical-align: top;
		font-size: 16px;
		line-height: auto;
		border-radius: 50%;
		background: #0F1330;
		width: 42px;
		height: 42px;
	}

	.main-content .el-pagination /deep/ .el-pager {
		padding: 0;
		margin: 0;
		display: flex;
		vertical-align: top;
	}

	.main-content .el-pagination /deep/ .el-pager .number {
		cursor: pointer;
		padding: 0 0px;
		color: #000000;
		font-weight: 400;
		display: flex;
		vertical-align: top;
		font-size: 16px;
		line-height: auto;
		background: none;
		justify-content: center;
		align-items: center;
		text-align: center;
		min-width: 42px;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .el-pager .number:hover {
		cursor: pointer;
		padding: 0 0px;
		color: #FFFFFF;
		font-weight: 400;
		display: flex;
		vertical-align: top;
		font-size: 16px;
		line-height: auto;
		border-radius: 50%;
		background: #6EADEF;
		align-items: center;
		text-align: center;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .el-pager .number.active {
		cursor: pointer;
		padding: 0px;
		color: #FFFFFF;
		font-weight: 400;
		display: flex;
		vertical-align: top;
		font-size: 16px;
		line-height: auto;
		border-radius: 50%;
		background: #6EADEF;
		justify-content: center;
		align-items: center;
		text-align: center;
		min-width: 42px;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes {
		margin: 0 0px 0 0;
		display: inline-block;
		vertical-align: top;
		font-size: 16px;
		line-height: 42px;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input {
		margin: 0 5px;
		width: 100px;
		position: relative;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__inner {
		border: 1px solid #DCDFE6;
		cursor: pointer;
		padding: 0 25px 0 8px;
		color: #606266;
		display: inline-block;
		font-size: 16px;
		line-height: 28px;
		border-radius: 3px;
		outline: 0;
		background: #FFF;
		width: 100%;
		text-align: center;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input span.el-input__suffix {
		top: 0;
		position: absolute;
		right: 0;
		height: 100%;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
		cursor: pointer;
		color: #C0C4CC;
		width: 25px;
		font-size: 14px;
		line-height: 48px;
		text-align: center;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__jump {
		margin: 0 0 0 24px;
		color: #606266;
		display: inline-block;
		vertical-align: top;
		font-size: 16px;
		line-height: 42px;
		height: 42px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input {
		border-radius: 3px;
		padding: 0 2px;
		margin: 0 2px;
		display: inline-block;
		width: 50px;
		font-size: 14px;
		line-height: 18px;
		position: relative;
		text-align: center;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input .el-input__inner {
		border: 1px solid #DCDFE6;
		cursor: pointer;
		padding: 0 3px;
		color: #606266;
		display: inline-block;
		font-size: 16px;
		line-height: 28px;
		border-radius: 3px;
		outline: 0;
		background: #FFF;
		width: 100%;
		text-align: center;
		height: 28px;
	}
	
	// list one
	.one .list1-view {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 15px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #fff;
		background: #157ed2;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.one .list1-view:hover {
		opacity: 0.8;
	}
	
	.one .list1-edit {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 15px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #fff;
		background: #409eff;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.one .list1-edit:hover {
		opacity: 0.8;
	}
	
	.one .list1-del {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 15px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #fff;
		background: rgba(255, 0, 0, 1);
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.one .list1-del:hover {
		opacity: 0.8;
	}
	
	.one .list1-btn8 {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 24px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #fff;
		background: rgba(255, 128, 0, 1);
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.one .list1-btn8:hover {
		opacity: 0.8;
	}
	
	.main-content .el-table .el-switch {
		display: inline-flex;
		vertical-align: middle;
		line-height: 30px;
		position: relative;
		align-items: center;
		height: 30px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__label--left {
		cursor: pointer;
		margin: 0 10px 0 0;
		color: #333;
		font-weight: 500;
		display: none;
		vertical-align: middle;
		font-size: 16px;
		transition: .2s;
		height: 30px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__label--right {
		cursor: pointer;
		margin: 0 0 0 10px;
		color: #333;
		font-weight: 500;
		display: none;
		vertical-align: middle;
		font-size: 16px;
		transition: .2s;
		height: 30px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__core {
		border: 1px solid #75c0d6;
		cursor: pointer;
		border-radius: 15px;
		margin: 0;
		background: #75c0d6;
		display: inline-block;
		width: 42px;
		box-sizing: border-box;
		transition: border-color .3s,background-color .3s;
		height: 20px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__core::after {
		border-radius: 100%;
		top: 1px;
		left: 1px;
		background: #fff;
		width: 16px;
		position: absolute;
		transition: all .3s;
		height: 16px;
	}
	.main-content .el-table .el-switch.is-checked /deep/ .el-switch__core::after {
		margin: 0 0 0 -18px;
		left: 100%;
	}
	
	.main-content .el-table .el-rate /deep/ .el-rate__item {
		cursor: pointer;
		display: inline-block;
		vertical-align: middle;
		font-size: 0;
		position: relative;
	}
	.main-content .el-table .el-rate /deep/ .el-rate__item .el-rate__icon {
		margin: 0 3px;
		display: inline-block;
		font-size: 18px;
		position: relative;
		transition: .3s;
	}

</style>
