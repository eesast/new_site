<template>
  <div id="wrap">
    <el-form :model="form" :rules="rules" ref="form" label-width="100px">
      <el-form-item prop="realname" label="真实姓名">
        <el-input v-model="form.realname"></el-input>
      </el-form-item>
      <el-form-item prop="class" label="班级">
        <el-input v-model="form.class"></el-input>
      </el-form-item>
      <el-form-item prop="sex" label="性别">
        <el-radio v-model="form.sex" label="1">男</el-radio>
        <el-radio v-model="form.sex" label="2">女</el-radio>
      </el-form-item>
      <el-form-item prop="studentid" label="学号">
        <el-input v-model="form.studentid"></el-input>
      </el-form-item>
      <el-form-item prop="ethnic" label="民族">
        <el-input v-model="form.ethnic"></el-input>
      </el-form-item>
      <el-form-item prop="politic" label="政治面貌">
        <el-select v-model="form.politic" placeholder="请选择">
          <el-option
            v-for="item in politics"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item> 
      <el-form-item prop="phone" label="手机号">
        <el-input v-model="form.phone"></el-input>
      </el-form-item>
      <el-form-item prop="email" label="邮箱">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item prop="dorm" label="宿舍号">
        <el-input v-model="form.dorm"></el-input>
      </el-form-item>
      <el-form-item prop="birthday" label="生日">
        <el-date-picker
          v-model="form.birthday"
          type="date"
          default-value="1999-01-01"
          placeholder="选择日期">
        </el-date-picker>
      </el-form-item>
      <el-form-item prop="depart1" label="部门一意愿">
        <el-select v-model="form.depart1" placeholder="请选择">
          <el-option
            v-for="item in departments"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="depart2" label="部门二意愿">
        <el-select v-model="form.depart2" placeholder="请选择">
          <el-option
            v-for="item in departments"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="depart3" label="部门三意愿">
        <el-select v-model="form.depart3" placeholder="请选择">
          <el-option
            v-for="item in departments"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="hobby" label="兴趣爱好">
        <el-input
          type="textarea"
          :rows="2"
          placeholder="请输入内容"
          v-model="form.hobby">
        </el-input>
      </el-form-item>
      <el-form-item prop="skill" label="技术特长">       
        <el-input
          type="textarea"
          :rows="2"
          placeholder="请输入内容"
          v-model="form.skill">
        </el-input>
      </el-form-item>
      <el-button type="primary" @click="submit">提交</el-button> 
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data(){
      return {
        form: {
          realname: ''
        },
        rules: {
          realname: [
            {required: true, message: '请输入姓名', trigger: 'blur'}
          ],
          class: [
            {required: true, message: '请输入班级', trigger: 'blur'}
          ],
          sex: [
            {required: true, message: '请选择', trigger: 'blur'}
          ],
          email: [
            {required: true, message: '请输入邮箱', trigger: 'blur'}
          ],
          dorm: [
            {required: true, message: '请输入邮箱', trigger: 'blur'}
          ],
          birthday: [
            {required: true, message: '请输入邮箱', trigger: 'blur'}
          ],
          depart1: [
            {required: true, message: '请选择部门', trigger: 'blur'}
          ],
          depart2: [
            {required: true, message: '请选择部门', trigger: 'blur'}
          ],
          depart3: [
            {required: true, message: '请选择部门', trigger: 'blur'}
          ],
        },
        politics: [
          {value: 1, label: '党员'},
          {value: 2, label: '预备党员'},
          {value: 3, label: '共青团员'},
          {value: 4, label: '非团员'},
        ],
        departments: [
          {value: 1, label: '网宣部'},
          {value: 2, label: '软件部'},
          {value: 3, label: '硬件部'},
          {value: 4, label: '项目部'},
          {value: 5, label: '学培部'},
        ]
      }
  },
  computed:{
    depart(iter){
      return "depart"+iter
    },
    depart1(iter){
      return "部门意愿"+iter
    }
  },
  methods: {
    submit(){

    }
  }
}
</script>

<style scoped>
  .el-form-item{
    text-align: left;
    width: 320px;
  }
  .el-input{
    display: inline-block;
  }
</style>
