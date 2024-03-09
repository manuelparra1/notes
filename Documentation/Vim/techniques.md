### Insert Characters To Each Line$

1. `<C-v>` select characters of each line.
2. `<S-I>` enter character `<Esc>`
3. Vim will insert character to each line.

```vim
# Inserting "1. " to each line
<C-v>4j1. <Esc>
```

```text
1. A sample sentence.
1. A sample sentence.
1. A sample sentence.
1. A sample sentence.
1. A sample sentence.
```

### Increment Visually Selected Characters

1. `<C-v>` select characters of each line.
2. `g<C-a>`
3. Vim will increment visually selected characters.

```vim
# Incrementing visually selected characters
<C-v>4jg<C-a>
```

```text
1. A sample sentence.
1. A sample sentence.
1. A sample sentence.
1. A sample sentence.
1. A sample sentence.

# Tranforms to:

1. A sample sentence.
2. A sample sentence.
3. A sample sentence.
4. A sample sentence.
5. A sample sentence.
```

# Search For Visually Selected Characters

1. `<C-v>` # Select characters of each line.
2. `y` # Copy selected text
3. `/` # Enter search mode
4. `<C-r>"` # Insert text from " register
5. `Enter` # Results
