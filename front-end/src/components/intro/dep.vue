<template>
    <div class="wrap">
        <h1>部门介绍</h1>
        <div class="dep software">
            <div class="article">
                <p>
                    软件部，致力于提升技术水平，让同学们体会开发的乐趣，是同学们走向编程大佬之路的踏脚石。
                </p>
                <p>
                    新一年的软件部借鉴前人的经验教训，有着更广阔的技术领域。在“暑期培训”中，打下坚实广泛的基础；在黑框界面和高亮代码中，操控整个服务器的运行；“学生节直播”，带你走进网络编程的世界；在“AI挑战赛开发”，体验团队协作的开发模式，了解团体项目开发流程，享受做出大工程的成就感。
                </p>
                <p>
                    此外，还有定期技术交流，让你结识更多志同道合的伙伴；微信公众号技术分享，为全电子系的同学普及知识。
                </p>
                <p>
                    如果你喜欢编程，喜欢开发，来加入软件部吧，迈出你成为大佬的又一步。
                </p>
                <img src="/static/img/s-d.jpg"/>
            </div>
            <div class="title">
                <h2>软件部</h2>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "dep",
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
.dep {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
}
.article {
    order: 1;
    padding: 3% 10%;
    text-align: left;
}
.title {
    order: 2;
    width: 60%;
    margin: 3% 0;
    border-left: solid 5px rgba(100,100,100,0.5);
}
</style>
