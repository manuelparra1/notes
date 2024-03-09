### Copy files from `fd` results to Directory

```bash
fd -g "Test*.md" | xargs -I % cp % Udemy-Guide/
```
