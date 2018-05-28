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
                <div class='img-wrap'>
                    <img src='../../../static/img/sdc.png'/>
                    <p class='ia'>第一届软件设计大赛宣传海报</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import '../../../static/css/article.css';
import IntroTitle from './IntroTitle';
export default {
    name: 'sdc',
    components: { IntroTitle },
}
</script>