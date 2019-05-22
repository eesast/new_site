<template>
    <div class='wrap'>
        <intro-title i-title='软件设计大赛'></intro-title>
        <div class='content'>
            <div class='article'>
                <h4>简要介绍</h4>
                <p>
                    软件设计大赛要求参赛者使用当今主流的技术栈，面向某个特定需求，完成一套具备一定可用性和美观性的软件程序。
                    对于“软件”的定义十分宽泛，游戏、网站、APP 都可以作为作品提交。
                </p>
                <h4>参赛要求</h4>
                <p>
                    • 参赛者以个人为单位参加比赛。每名同学也可提交不超过 2 个作品。
                </p>    
                <p>
                    • 参赛选手应当是清华大学在校学生。
                </p>
                <p>
                    • 参赛者应当在指定时间内以指定的方式完成队伍报名和程序提交。
                </p>
                <h4>作品要求</h4>
                <h6>美观性</h6>
                <p>
                    提交作品需要对UI(user interface) 有基本的设计，具有一定的美观性。
                </p>
                <h6>功能性</h6>
                <p>提交作品需要针对某一类需求，提供一种解决方案。</p>
                <h6>原创性</h6>
                <p>提交作品应当是小组的原创作品。</p>
                <h6>稳定性</h6>
                <p>提交作品需要具有一定的稳定性，尽可能的减少异常和出错的概率。</p>
                <br/>
                <br/>
                <h4>精彩回顾</h4>
                <p>2018年软件设计大赛优秀作品： </p>             
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc/calcpro.png'/>
                    <p class='ia'>多功能计算器CalcPro</p>
                </div>
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc/BASIC-OS1.jpg'/>
                    <p class='ia'>简易操作系统BASIC-OS1</p>
                </div>
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc/Net-Campus.jpg'/>
                    <p class='ia'><a href="https://www.microsoft.com/store/apps/9PDVWNT4K1MW" target="_blank">校园网管理软件Net-Campus</a></p>
                </div>
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc/ernie.png'/>
                    <p class='ia'><a href="http://www.raineggplant.com/ernie.html/" target="_blank">随机抽签软件Ernie</a></p>
                </div>
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc/cube-helper.jpg'/>
                    <p class='ia'>魔方助手Cube Helper</p>
                </div>
                <br/><br/><br/><br/>
                <p>2019年软件设计大赛优秀作品： </p>             
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc/musicgame.png'/>
                    <p class='ia'><a href="http://www.tunestory.cn" target="_blank">音乐节奏游戏TuneStory</a></p>
                </div>
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc/lowpoly.png'/>
                    <p class='ia'>三角形滤镜LowPoly</p>
                </div>
                 <div class='img-wrap'>
                    <img src='../../../static/img/sdc/plotter.png'/>
                    <p class='ia'><a href="http://www.johnao.tk/plotter" target="_blank">在线多功能绘图</a></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import '../../../static/css/article.css';
import IntroTitle from './IntroTitle';
export default {
    name: 'sdc',
    components: { IntroTitle },
}
</script>
<style scoped>
@import '../../../static/css/article.css';
</style>