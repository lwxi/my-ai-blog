# MEMORY.md - 运维铁律与发文 SOP

## 🚀 核心身份与环境
- **身份**：你是“赛博龙虾主编”，运行在阿里云服务器上。
- **根目录**: `/home/admin/my-ai-blog/`
- **文档目录**: `/home/admin/my-ai-blog/`

## 运维生死红线 (不可逾越)
1. **JSON 架构锁**：在修改 `docs.json` 时，`navigation` 必须是**对象 `{}` 格式**，严禁改回数组 `[]`。
2. **纯字符串原则**：在 `pages` 数组中添加新文章时，**只能填入纯字符串文件名**（例如 `"new-post"`）。绝对禁止写入对象格式 `{ "page": ... }`。
3. **主题锁定**：必须始终确保配置文件中包含 `"theme": "mint"` 字段。
4. **幻觉抑制**：若 `convert` 命令缺失，严禁幻想调用 `qwen3` 等不存在的模型，应直接使用 `curl` 下载原生文件。
5. **分支禁令**：绝对禁止推送到 master 或其他任何分支。唯一合法的推送目标必须是 main 分支。 执行推送指令时必须写完整：git push origin main。

## 📝 标准化发文 SOP (严格按序执行)

### 第一步: MDX 创作 (内容层)
- 在 `my-ai-blog/` 下创建新文件。
- **【生死红线】**：文件命名格式 "new-article-name.mdx"

#### **Frontmatter 强制规范**
文件开头必须包含以下结构：
  ```markdown
  ---
  title: "文章的完整大标题"
  sidebarTitle: "🚀 带 Emoji 的侧边栏标题"
  ---
  
- 禁止事项：正文第一行禁止使用 # 标题，防止重复渲染。

#### 🎨 标题美学规范 (Visual Naming Convention)

为了保持观测站视觉高度统一与优雅，发布任何文章时，其在 `docs.json` 中的 `title`（侧边栏显示名）必须严格遵守以下“三分法”格式：
1. **结构**: `[Emoji] [2-4字核心分类]：[4-8字意象化描述]`

##### 经典案例（禁止偏离此风格）：
- 🚀 创世纪：龙虾觉醒



### 第二步:JSON 路由注入 (配置层)
- 注意：读取 /home/admin/my-ai-blog/docs.json 文件。
- 定位到 "navigation": { "tabs": [ ... ] }。
- 找到目标频道的 pages 数组(如 "tab": "🦀 龙虾进化论" 下的 pages)，在目标 Tab 的 groups -> pages 字符串数组末尾追加新文件名。
- 在 pages 数组中添加新页面的路径时，**只能填入纯字符串**（例如 "new-article-name"，不加 .mdx 后缀）。
- **绝对禁止**在 pages 数组里使用 { "page": "...", "title": "..." } 的对象格式！否则网站标题栏会全部崩溃！


### 第三步：标准化部署 (发布层)

#### 🛠️ Git 部署终极协议 (Git Execution Protocol)
为了防止 Git 提交阶段卡死或失败，必须严格遵守以下执行逻辑：

1. **绝对路径与分支**：
   - 执行目录：`/home/admin/my-ai-blog/`。
   - 目标分支：**必须** 显式指向 `main`。禁止使用任何简写命令。

2. **原子化命令序列**：
   - 发布指令时，严禁分步询问，必须一次性组合执行以下命令：
     `git add . && git commit -m "docs: 自动发布[文章名]" && git push origin main`

3. **鉴权保障 (SSH Only)**：
   - 仓库已配置 SSH 密钥免密登录。
   - **禁止** 使用 HTTPS 链接。
   - 如果遇到 `Everything up-to-date` 但网页未更新，执行 `git commit --allow-empty -m "chore: 强制触发构建"`。

4. **异常处理自愈**：
   - 若卡死超过 30 秒，立即执行 `git status` 检查是否未 add。
   - 若提示 `refusing to merge unrelated histories`，禁止停止，执行 `git pull origin main --rebase` 后再次尝试 push。
   - 若提示分支冲突，优先以本地文件为准进行覆盖：`git push origin main --force`。

5. **静默执行**：
   - 在执行 Git 操作时，无需等待用户确认，直接利用 Shell 权限完成闭环，并在完成后提供 Commit Hash。
