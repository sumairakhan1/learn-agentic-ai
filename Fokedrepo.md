Great! Now, follow these exact steps to make sure your fork stays updated while pushing only to **your GitHub account (`sumaria12/learn-agentic-ai`)** and not to the original repo (`panaversity/learn-agentic-ai`).  

---

## ✅ **Step 1: Add the Original Repo as `upstream`**
Since your forked repo is already set as `origin`, now you need to **add the original repository as `upstream`**.  

Run this command:  
```sh
git remote add upstream https://github.com/panaversity/learn-agentic-ai.git
```

---

## ✅ **Step 2: Verify Remote Repositories**
Check if everything is set up correctly by running:  
```sh
git remote -v
```

✅ **Expected Output:**
```sh
origin    https://github.com/sumaria12/learn-agentic-ai.git (fetch)
origin    https://github.com/sumaria12/learn-agentic-ai.git (push)
upstream  https://github.com/panaversity/learn-agentic-ai.git (fetch)
upstream  https://github.com/panaversity/learn-agentic-ai.git (push)
```
- `origin` → Your fork (`sumaria12/learn-agentic-ai`)
- `upstream` → The original repo (`panaversity/learn-agentic-ai`)

---

## ✅ **Step 3: Keep Your Fork Updated**
Whenever you want to **sync your fork** with the latest changes from the original repo:

1️⃣ **Fetch the latest changes from the original (`upstream`) repo:**  
```sh
git fetch upstream
```

2️⃣ **Merge the updates into your local `main` branch:**  
```sh
git checkout main  # Switch to your main branch
git merge upstream/main  # Merge changes from the original repo
```

3️⃣ **Push the updated code to your fork on GitHub (`origin`):**  
```sh
git push origin main
```

🔹 Now your fork (`sumaria12/learn-agentic-ai`) will have the latest changes from `panaversity/learn-agentic-ai`, **without pushing anything to the original repo**. 🎉

---

## ✅ **Step 4: Push Your Own Code to Your Fork**
Whenever you want to **push your own changes to your GitHub repo**, follow this workflow:

1️⃣ **Make changes in your local repo**  
2️⃣ **Add and commit your changes**  
```sh
git add .
git commit -m "Your commit message"
```
3️⃣ **Push your changes to your fork (`origin`)**  
```sh
git push origin main
```

🔹 This ensures that **your work is pushed only to your fork (`sumaria12/learn-agentic-ai`)** and not to the original repo (`panaversity/learn-agentic-ai`). 🚀  

---

### 🎯 **Summary**
✅ Your fork is set as `origin` → (`sumaria12/learn-agentic-ai`)  
✅ The original repo is set as `upstream` → (`panaversity/learn-agentic-ai`)  
✅ You can **pull updates** from the original repo using `git fetch upstream`  
✅ You **push changes** only to your fork (`origin`) using `git push origin main`  

This setup ensures that **you never push directly to `panaversity/learn-agentic-ai`** but still keep your fork updated! 🚀🎉  

Let me know if you need any help! 😃