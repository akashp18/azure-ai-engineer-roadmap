# Git Workflow Rule

**CRITICAL INSTRUCTION FOR ALL AI AGENTS:**

Whenever you are assisting with an exercise or project in this repository, you **MUST STRICTLY** follow this Git workflow:

1. **Branching:** Do not create or edit exercise code on the `main` branch. Create a new branch for the exercise (e.g., `git checkout -b exercise/06-env-errors`).
2. **Implementation:** Write the exercise code or project files on the new branch.
3. **Documentation:** Update all relevant tracking files to reflect the progress:
   - Mark the item as completed in `progress/roadmap.md`.
   - Update `progress/weekly-log.md` with what was learned.
   - If a phase is completed, update the main `README.md` progress bar.
4. **Commit:** Commit the code and the markdown updates to the exercise branch.
5. **Push and Merge:** Run the following commands to push the branch, merge it, and sync `main`:
   ```bash
   git push -u origin <branch-name>
   git checkout main
   git merge <branch-name>
   git push origin main
   ```
6. **Next Step:** Return to `main` or create the next branch before continuing work.

**Never skip this process.** This ensures every exercise has its own branch and PR history on the remote repository.
