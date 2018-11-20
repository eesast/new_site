<template>
    <div>
        <h1>培训资料</h1>
        <div id="wrap">
            <el-tabs id="train-card" tab-position="left" v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="0-python" name="first" id='card1'>
                <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>0-python</span>
                    <!-- <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button> -->
                </div>
                <div v-for="o in message" :key="o" class="text item">
                    <div v-html="'<li>'+o.mmd+'</li>'"></div>
                </div>
                </el-card>
            </el-tab-pane>
            <el-tab-pane label="1-linux" name="second" id='card2'>1-linux</el-tab-pane>
            <el-tab-pane label="2-djangp" name="third" id='card3'>2-djangp</el-tab-pane>
            <el-tab-pane label="3-html" name="fourth" id='card4'>3-html</el-tab-pane>
            <el-tab-pane label="4-Communication&Testing" name="fifth" id='card5'>4-Communication&Testing</el-tab-pane>
            <el-tab-pane label="5-git" name="sixth" id='card6'>5-git</el-tab-pane>
            <el-tab-pane label="7-C#&Unity" name="seventh" id='card7'>7-C#&Unity</el-tab-pane>
            </el-tabs>
        </div>
    </div>
</template>
<script>
export default {
    name: "train",
     data() {
      return {
        activeName: 'first',
        message:[
            {
                mmd:"<a href='/static/files/0-python/author.txt' download='author.txt'>author.txt</a>"
            },
            {
                mmd:"<a href='/static/files/0-python/python0.pdf' download='python0.pdf'>python0.pdf</a>"
            }
        ]
      };
    },
    methods: {
    //   handleClick(tab, event) {
    //     // console.log(tab, event);
    //   }
    }
}


</script>
<style lang="scss">
h1 {
    width: 70%;
    padding-bottom: 20px;
    display: inline-block;
    border-bottom: solid 1px rgba(120,120,120,0.4);
    font-size: 2.5rem;
}
h2 {
    font-size: 2rem;
}
p {
    margin-top: 0;
}
img {
    width: 80%;
    margin: 3% 11% 3% 9%;
}
#wrap {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
}
#train-card
{
    position: relative;
    width:80%;
    height:600px;
}
.el-tab-pane
{
    font-size:32px;
    // color:red;
}
.box-card
{
    height:600px;
}
.box-card a
{
    text-decoration:none; 
    color:black;
}
// #tab-first{
    
//     background: #b1b4bb;
// }
// #tab-second{
    
//     background: rgb(208, 212, 219);
// }
// #tab-third{
    
//     background: #DCDFE6;
// }
// #tab-fourth{
    
//     background: #E4E7ED;
// }
// #tab-fifth{
    
//     background: #EBEEF5;
// }
// #tab-sixth{
    
//     background: #F2F6FC;
// }
// #tab-seventh{
    
//     background: rgb(249, 250, 253);
// }

// .train {
//     width: 70%;
//     margin: 0 auto;
//     padding: 2% 0;
//     display: flex;
//     flex-direction: row;
//     justify-content: space-between;
//     align-items: flex-start;
//     border-top: solid 1px rgba(100,100,100,0.5);
// }
// .python {
//     border: none;
// }
/*
.hardware {
    order: 2;
}
.project {
    order: 3;
}
.study {
    order: 4;
}*/
// .article {
//     order: 1;
//     padding: 3% 10% 3% 2%;
//     text-align: left;
// }
.title {
    order: 2;
    width: 40%;
    margin: 3% 0;
    padding-left: 5%;
    border-left: solid 5px rgba(100,100,100,0.5);
}
</style>
