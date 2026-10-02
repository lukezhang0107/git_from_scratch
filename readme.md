aloha

# assignment 0 作业学习心得

## 1. 
掌握了各种 git 的基础概念，反复练习了使用 git 的基础指令：
- `git clone <repo_address> "local_directory"` 用于将远程仓库克隆到本地，
- `git branch` 查看分支，
- `git checkout <branch>` 切换分支（尽量避免 `git checkout <commit hash>`），
- `git checkout -b xxx` 创建分支，其中 `git checkout -b xxx <commit_hash>` 会从某一次提交创建分支，`git checkout -b xxx origin/other_branch` 会从远程的某一个分支创建，
- `git log --oneline` 查看提交历史和 commit hash，
- `git add` 进行暂存，
- `git commit -m` 提交并写入 message（push 前必须要有 commit）。没有学习前我觉得好像 `git commit` 和 `git push` 差不多，但是经过这次作业我终于分清了二者的区别，我感觉这个 commit 应该是 git 进行版本控制的核心，
- `git push origin main` 上传，
- `git status` 用于检查本地状态（未提交/提交但未 push/已 push），
- `git reflog` 用于查看 HEAD 移动历史，用于恢复误删的提交，
- `git show <commit>:<file path>` 用于查看文件内容
- `git bundle` 则用于打包整个仓库。

## 2. 
除了作业的要求之外，我还了解了其他指令的内容，比如 `git mv`（重命名），`git fetch`（只下载最新的远程提交，而不改动当前的工作区），`.gitignore` 文件用于忽略不想被跟踪的文件，以及不同情况下如何恢复之前的文件内容：
- 尚未 commit：`git restore -- <file name>`，
- 已经 commit 但还没 push：`git reset --hard <target commit hash>`
- 已经 push 到 GitHub 了：`git revert <target commit hash>`

## 3. 
巩固了 `pwd`、`cd`、`echo`、`cat`、`which`、`export`（在当前会话设置环境变量） 等基础指令的使用。`echo "content" > file_name` 是覆盖，`echo "content" >> file_name` 是追加。

## 4. 
理解了 `git merge` 的含义，以 `git merge for_fun` 为例，它会先找到 `main` 和 `for_fun` 的共同祖先提交，然后比较两个分支从共同祖先到各自最新提交的差异，再把 `for_fun` 中独有的改动应用到 main 上而不是全部替换。如果修改的是同一个文件的同一部分（比如都改了 `readme.md` 的第一行），就会产生冲突。

## 5. 
在 git bash 中使用 conda 管理环境。当 `conda activate` 无效时，需要运行 `conda init bash` 然后重启终端。
