# 换了电脑，怎样更新博客？
1. 本地的上传至github。
- 创建一个仓库。
- 创建两个分支：master与hexo。
- 设置hexo为默认分支。
- 使用git clone拷贝到本地，然后将电脑中本地搭建的整个博客文件夹拷贝到该仓库目录下，**然后将next主题文件夹下的.git与.gitignore文件删除掉**,否则会导致部署后页面为空。
- 依次执行npm install hexo、hexo init、npm install 和 npm install hexo-deployer-git。
- 依次执行git add . 、git commit -m "update"、git push origin hexo。
- 执行hexo g -d。
2. 从github上clone下来更新
- 依次执行npm install hexo、npm install 、 npm install hexo-deployer-git。
> index首页丢失解决方法：将.deploy_git删除，重新跑一遍1中npm ...。
