### Find all sentences that begin with a capital letter and end with a question mark.

```regex
:%s/\(^[A-Z].*?$\)/### \1/g
```
