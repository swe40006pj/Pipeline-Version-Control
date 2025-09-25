# Pipeline Demo
# 📘 Development Guide

## Branch Model
- **main**: Production branch  
  - Only accepts **Release Tags** or **hotfix PRs**  
- **develop**: Integration/Testing branch  
  - All feature branches merge into this branch  
- **feature/***: Feature branches  
  - Branch off from `develop` → develop features → PR → merge back into `develop`  

## Branch Protection & Merge Strategy
- **main**  
  - Direct pushes are **not allowed** (Require PR before merge)  
  - At least **1 reviewer** required  
  - Merge strategy: **Squash only ✅**, Merge commits disabled ❌  
- **develop**  
  - Direct pushes are **not allowed** (Require PR before merge)  
  - Reviewer requirement can be relaxed (0–1 reviewers)  
  - Use **Squash merge** to keep history clean  

## Branch Naming
- Features: `feature/<description>`  
- Bug fixes: `fix/<description>`  
- Maintenance (chore/docs/config): `chore/<description>`  
- Example: `feature/add-login`, `fix/api-bug`, `chore/update-deps`  

## Contribution Workflow
1. Switch to and update `develop`  
   ```bash
   git checkout develop && git pull origin develop
   ```
2. Create a new feature branch  
   ```bash
   git checkout -b feature/<name>
   ```
3. Develop and commit code  
   ```bash
   git add . && git commit -m "feat: <message>" && git push
   ```
4. Submit a Pull Request  
   - Target branch: `develop`  
5. Merge into `develop`  
   - Requires reviewer approval → Squash merge  
6. Release process  
   - Merge `develop` into `main`  
   - Tag a version, e.g. `v1.0.0`
