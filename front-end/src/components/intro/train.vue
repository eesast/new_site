<template>
    <div>
        <h1>培训资料</h1>
        <div id="wrap">
            <el-tabs id="train-card" tab-position="left" v-model="activeName" @tab-click="handleClick"> 
            <!-- <template v-if="dirs"> -->
            <el-tab-pane  v-for='(dir,index) in dirs' :label='dir.name' :name="index" id='card1'>
                <el-card  class="box-card">
                    <div slot="header" class="clearfix">
                    <span>{{dir.name}}</span>
                     </div>
                
                    <el-table
                    :data="dir.subdirs"
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
export default {
    name: "train",
    created()
    {
        // console.log(x);
        // fetch("http://127.0.0.1:8888/backend/lecture/dir/",
        fetch("http://future.eesast.com/backend/lecture/dir/",
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
    // fetch("http://127.0.0.1:8888/backend/lecture/subdir/"+this.dirs[i].name,
    fetch("http://future.eesast.com/backend/lecture/subdir/"+this.dirs[i].name,
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
            // x.download="<a href='../../../static/files/"+this.dirs[i].name+"/"+x.name+"' download='"+x.name+"'>立即下载</a>";
            x.download="<a href='../../../../lecture_files/"+this.dirs[i].name+"/"+x.name+"' download='"+x.name+"'>立即下载</a>";
            this.dirs[i].subdirs.push(x);
            console.log(x.download);
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
