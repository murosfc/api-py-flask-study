# Quick Git Commands for Deployment

## Check current status

```bash
git status
```

## Stage all files

```bash
git add .
```

## Commit changes

```bash
git commit -m "Configure project for Vercel deployment"
```

## Push to remote

```bash
git push origin main
```

## If you need to set remote (first time)

```bash
git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main
```

## Check remote

```bash
git remote -v
```

## After pushing, Vercel will automatically deploy! 🚀
