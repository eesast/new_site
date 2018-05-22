<template>
  <div class="footer">
    <div class="contact">
      <h4>联系我们</h4>
      <div class="contact_container">
        <a href="">
          <img src="..\..\static\github.svg"/>Github</a>
      </div>
      <div class="contact_container">
        <a href="">
          <img src=""/>Wechat</a>
      </div>
      
      
    </div>
    
    
    <div class="support">
      <h4>技术支持</h4>
      <a href="https://www.djangoproject.com/">
        <img src="../../static/django.svg" /></a>
      <a href="https://cn.vuejs.org/">
        <img src="../../static/vue.png"/></a>
      <a href="https://element.eleme.io/">
        <img src="../../static/elementui.svg"/></a>
      <a href="https://github.com/">
        <img src="../../static/github.svg"/></a>
    </div>
  </div>
</template>

<script>
export default {
  name: "foot"
};

</script>

<style scoped>.footer {
  width: 100%;
  height: 150px;
  display: flex;
  flex-direction: row;
}

.col {
  margin: 0;
  vertical-align: middle;
  box-sizing: content-box;
}

.contact {
  order: 1;
  width: 15%;
  padding: 0 4%;
  vertical-align: middle;
  text-align: center;
  align-items: flex-start;
}
.contact_container{
  margin-bottom: 12px;
}
.contact_container a{
  font-size: 20px;
}
.contact a {
  text-decoration: none;
  color: black;
}
a:visited a:hover {
  text-decoration: none;
}
a:hover{
  color: #303030da;
}
.contact p{
  margin-top: 0;
}
h4 {
  margin-bottom: 10px;
  padding-bottom: 10px;
  border-bottom: solid #f0f0f0 1px;
}

.contact_container img {
  width: 20px;
  vertical-align: top;
  margin-right: 5%;
}





.support {
  order: 4;
  width: 34%;
  padding: 0;
  text-align: center;
  align-items: flex-start;
}
.support h4{
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: solid #f0f0f0 1px;
}
.support img {
  width: 30px;
  height: 30px;
  vertical-align: middle;
  margin: 20px 1%;
}

</style>
