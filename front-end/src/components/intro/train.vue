<template>
    <div>
        <intro-title i-title='培训资料'></intro-title>
        <div id="wrap">
            <el-tabs id="train-card" tab-position="left" v-model="activeName" @tab-click="handleClick"> 
            <!-- <template v-if="dirs"> -->
            <el-tab-pane  v-for='(dir,index) in dirs' :label='dir.name.substring(2)' :name="index" id='card1'>
                <el-card  class="box-card">
                    <!-- <div slot="header" class="clearfix">
                    <span>{{dir.name.substring(2)}}</span>
                     </div> -->
                
                    <el-table
                    :data="dir.subdirs"
                    style="width: 100%">
                
                    <el-table-column
                        prop="name"
                        label="名称"
                        width="700" 
                        align="center">
                    </el-table-column>
                    <el-table-column
                        prop="download"
                        label="下载地址"
                        width="200"
                        align="center">
                        <template slot-scope="scope">
                        <div v-html="scope.row.download"></div>
                        </template>
                    </el-table-column>
                    </el-table>
                
                </el-card>
           </el-tab-pane>
            <!-- </template> -->
            <!-- <el-tab-pane label="0-python" name="first" id='card1'>
                <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>0-python</span>
                     </div>
                
                <el-table
                :data="tableData"
                style="width: 100%">
               
                <el-table-column
                    prop="name"
                    label="名称"
                    width="700">
                </el-table-column>
                <el-table-column
                    prop="download"
                    label="下载地址"
                    width="200">
                    <template slot-scope="scope">
                    <div v-html="scope.row.download"></div>
                    </template>
                </el-table-column>
                </el-table>
                
                </el-card>
            </el-tab-pane>  -->
            <!-- <el-tab-pane label="1-linux" name="second" id='card2'>1-linux</el-tab-pane>
            <el-tab-pane label="2-djangp" name="third" id='card3'>2-djangp</el-tab-pane>
            <el-tab-pane label="3-html" name="fourth" id='card4'>3-html</el-tab-pane>
            <el-tab-pane label="4-Communication&Testing" name="fifth" id='card5'>4-Communication&Testing</el-tab-pane>
            <el-tab-pane label="5-git" name="sixth" id='card6'>5-git</el-tab-pane>
            <el-tab-pane label="7-C#&Unity" name="seventh" id='card7'>7-C#&Unity</el-tab-pane> -->
            </el-tabs>
        </div>
    </div>
</template>

<script>
import IntroTitle from './IntroTitle';
export default {
    name: "train",
    components: { IntroTitle },
    created()
    {
        // console.log(x);
        // fetch("http://127.0.0.1:8000/backend/lecture/dir/",
        fetch("/backend/lecture/dir/",
         {
            method:'GET',
            headers:
            {
                'Content-Type':'application/json',
            }
         }).then(response=>{
             if(response.ok)
             {
                 return response.json();
             }
         }).then(res=>
         {
             
             for(var i=0;i<res.dir.length;i++)
             {
                 this.dirs[i]=new Object();
                //  this.$set(this.dirs,i,{name:res.dir[i]});
                 this.dirs[i].name=res.dir[i];
                 this.GETSUB(i);
             }
         })
    },
     data() {
         
         
        //  var dirs=[{name:'0-python',tableData:[
        //     {
        //         name:'author.txt',
        //         download:"<a href='/static/files/0-python/author.txt' download='author.txt'>立即下载</a>"
                
        //     },

        return {
        activeName: '0',
        dirs:new Array(),
        // subdirs:new Array(),
      };
    },
    methods: {
      handleClick(tab, event) {
        // console.log(tab, event);
      },
        GETSUB(i)
{
    // fetch("http://127.0.0.1:8000/backend/lecture/subdir/"+this.dirs[i].name,
    fetch("/backend/lecture/subdir/"+this.dirs[i].name,
    {
        method:'GET',
        headers:
        {
            'Content-Type':'application/json',
        }
    }).then(respo=>
    {
        if(respo.ok)
        {
            return respo.json();
        }
    }).then(resp=>
    {
        this.dirs[i].subdirs=new Array(); 
        for(var j=0;j<resp.dir.length;j++)
        {
            // this.subdirs[i][j]=new Object();
            var x=new Object();
            x.name=resp.dir[j];;
            // x.download="<a href='../../../../../files/"+this.dirs[i].name+"/"+x.name+"' download='"+x.name+"'>立即下载</a>";
            x.download="<a href='../../../../lecture_files/"+this.dirs[i].name+"/"+x.name+"' download='"+x.name+"'>立即下载</a>";
            this.dirs[i].subdirs.push(x);
            // console.log(x.download);
            // console.log(this.dirs[i].subdirs[j]);
            // this.subdirs[i][j].name=resp.dir[j];
            // this.subdirs[i][j].download="<a href='/static/files/"+this.dirs[i]+"/"+this.subdirs[i][j].name+"' download='"+this.subdirs[i][j].name+"'>立即下载</a>"
        }
        this.$set(this.dirs,i,{name:this.dirs[i].name,subdirs:this.dirs[i].subdirs});
            
        // for (var dir in this.dirs)
        // {
        //     console.log(dir.name);
        //     console.log(dir.subdirs);
        // }
        
    }).then(()=>
             {
            //      for(var i=0;i<this.subdirs.length;i++)
            //  {
            //      console.log(this.subdirs);
            //  }
            // Vue.set(this.subdirs[0][0],'ok',1);
            // console.log(this.subdirs[6]);
             }
         )
}
    }
}

</script>
<style lang="scss" scoped>
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
.title {
    order: 2;
    width: 40%;
    margin: 3% 0;
    padding-left: 5%;
    border-left: solid 5px rgba(100,100,100,0.5);
}

#wrap {
    margin-top: 2%;
}

#train-card .el-tabs__item
{
    // color:red;
    border-bottom:0.5px solid rgb(241, 245, 250);
    // position:absolute;
    left:0;
    font-family:'Microsoft YaHei';
    // color:green;
    font-weight: 600;
    font-size:15px;
    text-align: center;
}
#train-card .el-tabs__item:hover
{
    background:#95c6f8;
    color:white;
    text-align: center;
}
#train-card .el-tabs__item:active
{
    background:#95c6f8;
    color:yellow;
    text-align: center;
}

.el-tabs--left .el-tabs__item.is-left {
    text-align: center;
}

.clearfix
{
    font-family: 'Times New Roman';
    font-weight: 500;
    font-size:40px;
}
.el-table__body .el-table__row
{
    font-family: 'Times New Roman';
    font-weight: 500;
    color:rgb(59, 52, 126);
}
</style>
