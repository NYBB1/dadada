<template>
	<div class="addEdit-block">
		<el-form
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
		>
			<template >
				<el-form-item class="input" v-if="type!='info'"  label="学号" prop="studentid" >
					<el-input v-model="ruleForm.studentid" placeholder="学号" clearable  :readonly="ro.studentid"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="学号" prop="studentid" >
					<el-input v-model="ruleForm.studentid" placeholder="学号" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="政治成绩" prop="politicalachievements" >
					<el-input-number v-model="ruleForm.politicalachievements" placeholder="政治成绩" :disabled="ro.politicalachievements"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="政治成绩" prop="politicalachievements" >
					<el-input v-model="ruleForm.politicalachievements" placeholder="政治成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="语文成绩" prop="chinesescores" >
					<el-input-number v-model="ruleForm.chinesescores" placeholder="语文成绩" :disabled="ro.chinesescores"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="语文成绩" prop="chinesescores" >
					<el-input v-model="ruleForm.chinesescores" placeholder="语文成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="数学成绩" prop="mathematicsgrades" >
					<el-input-number v-model="ruleForm.mathematicsgrades" placeholder="数学成绩" :disabled="ro.mathematicsgrades"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="数学成绩" prop="mathematicsgrades" >
					<el-input v-model="ruleForm.mathematicsgrades" placeholder="数学成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="外语成绩" prop="foreignlanguagescore" >
					<el-input-number v-model="ruleForm.foreignlanguagescore" placeholder="外语成绩" :disabled="ro.foreignlanguagescore"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="外语成绩" prop="foreignlanguagescore" >
					<el-input v-model="ruleForm.foreignlanguagescore" placeholder="外语成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="物理成绩" prop="achievement" >
					<el-input-number v-model="ruleForm.achievement" placeholder="物理成绩" :disabled="ro.achievement"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="物理成绩" prop="achievement" >
					<el-input v-model="ruleForm.achievement" placeholder="物理成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="化学成绩" prop="chemistrygrades" >
					<el-input-number v-model="ruleForm.chemistrygrades" placeholder="化学成绩" :disabled="ro.chemistrygrades"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="化学成绩" prop="chemistrygrades" >
					<el-input v-model="ruleForm.chemistrygrades" placeholder="化学成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="地理成绩" prop="geographyscore" >
					<el-input-number v-model="ruleForm.geographyscore" placeholder="地理成绩" :disabled="ro.geographyscore"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="地理成绩" prop="geographyscore" >
					<el-input v-model="ruleForm.geographyscore" placeholder="地理成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="历史成绩" prop="historicalachievements" >
					<el-input-number v-model="ruleForm.historicalachievements" placeholder="历史成绩" :disabled="ro.historicalachievements"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="历史成绩" prop="historicalachievements" >
					<el-input v-model="ruleForm.historicalachievements" placeholder="历史成绩" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="平均成绩" prop="averagescore" >
					<el-input-number v-model="ruleForm.averagescore" placeholder="平均成绩" :disabled="ro.averagescore"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="平均成绩" prop="averagescore" >
					<el-input v-model="ruleForm.averagescore" placeholder="平均成绩" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan"></span>
					提交
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

	</div>
</template>
<script>
	import { 
		isNumber,
	} from "@/utils/validate";
	export default {
		data() {
			var validateNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isNumber(value)) {
					callback(new Error("请输入数字"));
				} else {
					callback();
				}
			};
			return {
				id: '',
				type: '',
			
			
				ro:{
					studentid : false,
					politicalachievements : false,
					chinesescores : false,
					mathematicsgrades : false,
					foreignlanguagescore : false,
					achievement : false,
					chemistrygrades : false,
					geographyscore : false,
					historicalachievements : false,
					averagescore : false,
				},
			
				ruleForm: {
					studentid: '',
					politicalachievements: '',
					chinesescores: '',
					mathematicsgrades: '',
					foreignlanguagescore: '',
					achievement: '',
					chemistrygrades: '',
					geographyscore: '',
					historicalachievements: '',
					averagescore: '',
				},

				rules: {
					studentid: [
					],
					politicalachievements: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					chinesescores: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					mathematicsgrades: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					foreignlanguagescore: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					achievement: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					chemistrygrades: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					geographyscore: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					historicalachievements: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					averagescore: [
						{ validator: validateNumber, trigger: 'blur' },
					],
				},
			};
		},
		props: ["parent"],
		computed: {



		},
		components: {
		},
		created() {
		},
		methods: {
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(id,type) {
				if (id) {
					this.id = id;
					this.type = type;
				}
				if(this.type=='info'||this.type=='else'||this.type=='msg'){
					this.info(id);
				}else if(this.type=='logistics'){
					for(let x in this.ro) {
						this.ro[x] = true
					}
					this.logistics=false;
					this.info(id);
				}else if(this.type=='cross'){
					var obj = this.$storage.getObj('crossObj');
					for (var o in obj){
						if(o=='studentid'){
							this.ruleForm.studentid = obj[o];
							this.ro.studentid = true;
							continue;
						}
						if(o=='politicalachievements'){
							this.ruleForm.politicalachievements = obj[o];
							this.ro.politicalachievements = true;
							continue;
						}
						if(o=='chinesescores'){
							this.ruleForm.chinesescores = obj[o];
							this.ro.chinesescores = true;
							continue;
						}
						if(o=='mathematicsgrades'){
							this.ruleForm.mathematicsgrades = obj[o];
							this.ro.mathematicsgrades = true;
							continue;
						}
						if(o=='foreignlanguagescore'){
							this.ruleForm.foreignlanguagescore = obj[o];
							this.ro.foreignlanguagescore = true;
							continue;
						}
						if(o=='achievement'){
							this.ruleForm.achievement = obj[o];
							this.ro.achievement = true;
							continue;
						}
						if(o=='chemistrygrades'){
							this.ruleForm.chemistrygrades = obj[o];
							this.ro.chemistrygrades = true;
							continue;
						}
						if(o=='geographyscore'){
							this.ruleForm.geographyscore = obj[o];
							this.ro.geographyscore = true;
							continue;
						}
						if(o=='historicalachievements'){
							this.ruleForm.historicalachievements = obj[o];
							this.ro.historicalachievements = true;
							continue;
						}
						if(o=='averagescore'){
							this.ruleForm.averagescore = obj[o];
							this.ro.averagescore = true;
							continue;
						}
					}
				}
				// 获取用户信息
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						var json = data.data;
					} else {
						this.$message.error(data.msg);
					}
				});
			
			},
			// 多级联动参数

			info(id) {
				this.$http({
					url: `examresultsforecast1/info/${id}`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.ruleForm = data.data;
						//解决前台上传图片后台不显示的问题
						let reg=new RegExp('../../../upload','g')//g代表全部
					} else {
						this.$message.error(data.msg);
					}
				});
			},

			// 提交
			async onSubmit() {
					var objcross = this.$storage.getObj('crossObj');
					if(!this.ruleForm.id) {
						delete this.ruleForm.userid
					}
					await this.$refs["ruleForm"].validate(async valid => {
						if (valid) {
							if(this.type=='cross'){
								var statusColumnName = this.$storage.get('statusColumnName');
								var statusColumnValue = this.$storage.get('statusColumnValue');
								if(statusColumnName!='') {
									var obj = this.$storage.getObj('crossObj');
									if(statusColumnName && !statusColumnName.startsWith("[")) {
										for (var o in obj){
											if(o==statusColumnName){
												obj[o] = statusColumnValue;
											}
										}
										var table = this.$storage.get('crossTable');
										await this.$http({
											url: `${table}/update`,
											method: "post",
											data: obj
										}).then(({ data }) => {});
									}
								}
							}
							
							await this.$http({
								url: `examresultsforecast1/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(async ({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.examresultsforecast1CrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
								}
							});
						}
					});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.parent.showFlag = true;
				this.parent.addOrUpdateFlag = false;
				this.parent.examresultsforecast1CrossAddOrUpdateFlag = false;
				this.parent.contentStyleChange();
			},
		}
	};
</script>
<style lang="scss" scoped>
	.addEdit-block {
		padding: 70px 40px 0 90px;
	}
	.add-update-preview {
		padding: 30px 20% 30px 15%;
		margin: 0 20px;
		flex-direction: row;
		background: none;
		display: flex;
		width: 100%;
		border-color: #eee;
		border-width: 0px 0 0;
		border-style: solid;
		flex-wrap: wrap;
	}
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	.add-update-preview /deep/ .el-form-item {
		border: 1px solid #CBCBCB;
		padding: 0;
		flex-direction: row;
		background: #fff;
		display: block;
		width: 100%;
		justify-content: flex-start;
	}
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 10px;
		margin: 0;
		color: #000;
		background: #fff;
		font-weight: 400;
		width: 180px;
		font-size: 16px;
		line-height: 34px;
		text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 180px;
	}
	.add-update-preview .el-form-item span.text {
		border: 0px solid #CBCBCB;
		cursor: pointer;
		padding: 0 15px;
		margin: 0;
		color: #000;
		display: inline-block;
		font-size: 15px;
		line-height: 34px;
		border-radius: 0px;
		word-break: break-all;
		background: #fff;
		width: 100%;
		text-align: left;
		height: auto;
	}
	
	.add-update-preview .el-input {
		width: 100%;
	}
	.add-update-preview .el-input /deep/ .el-input__inner {
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 12px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input /deep/ .el-input__inner[readonly="readonly"] {
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 12px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input-number {
		text-align: left;
		width: 100%;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 12px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .is-disabled .el-input__inner {
		text-align: left;
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 12px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	.add-update-preview .el-select {
		width: 100%;
	}
	.add-update-preview .el-select /deep/ .el-input__inner {
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 10px;
		color: #000;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-select /deep/ .is-disabled .el-input__inner {
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 10px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-date-editor {
		width: 100%;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 10px 0 30px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
		border: 0px solid #CBCBCB;
		border-radius: 0px;
		padding: 0 10px 0 30px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 40px;
	}
	.add-update-preview .viewBtn {
		border: 0px solid #CBCBCB;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .viewBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .downBtn {
		border: 0px solid #CBCBCB;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .downBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .unBtn {
		border: 0px solid #CBCBCB;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0;
		color: #666;
		background: #fff;
		width: 100%;
		font-size: 15px;
		line-height: 34px;
		text-align: left;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #fff;
			display: none;
			font-size: 14px;
			height: 34px;
		}
	}
	.add-update-preview .unBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
		border:  1px solid #CBCBCB;
		cursor: pointer;
		border-radius: 5px  ;
		margin: 5px 0 0 10px;
		color: #666;
		background: #fff;
		object-fit: cover;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
		border:  1px solid #CBCBCB;
		cursor: pointer;
		border-radius: 5px  ;
		margin: 5px 0 0 10px;
		color: #666;
		background: #fff;
		object-fit: cover;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
		border:  1px solid #CBCBCB;
		cursor: pointer;
		border-radius: 5px  ;
		margin: 5px 0 0 10px;
		color: #666;
		background: #fff;
		object-fit: cover;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	.add-update-preview /deep/ .el-upload__tip {
		margin: 0 0 0 10px;
		color: #666;
		font-size: 15px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
		border: 0px solid #CBCBCB;
		border-radius: 5px;
		padding: 12px;
		color: #000;
		background: #fff;
		width: 100%;
		font-size: 14px;
		min-width: 514px;
		height: 120px;
	}
	.add-update-preview .el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
				border: 0px solid #CBCBCB;
				border-radius: 5px;
				padding: 12px;
				color: #000;
				background: #fff;
				width: 100%;
				font-size: 14px;
				min-width: 514px;
				height: 120px;
			}
	.add-update-preview .el-form-item.btn {
		padding: 0;
		margin: 0;
		.btn1 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 5px;
			padding: 0 10px;
			margin: 0 30px 0 20px;
			color: #000;
			background: #AFD0F5;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn1:hover {
			opacity: 0.8;
		}
		.btn2 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 5px;
			padding: 0 10px;
			margin: 0 30px 0 20px;
			color: #000;
			background: #AFD0F5;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 34px;
			}
		}
		.btn2:hover {
			opacity: 0.8;
		}
		.btn3 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 5px;
			padding: 0 10px;
			margin: 0 30px 0 20px;
			color: #000;
			background: #AFD0F5;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn3:hover {
			opacity: 0.8;
		}
		.btn4 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 5px;
			padding: 0 10px;
			margin: 0 30px 0 20px;
			color: #000;
			background: #AFD0F5;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn4:hover {
			opacity: 0.8;
		}
		.btn5 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 5px;
			padding: 0 10px;
			margin: 0 30px 0 20px;
			color: #000;
			background: #AFD0F5;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn5:hover {
			opacity: 0.8;
		}
	}
</style>
