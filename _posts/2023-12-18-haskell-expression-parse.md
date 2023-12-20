---
title: Haskell实现表达式求值
date: 2023-12-18 06:30:07
img_path: /_posts/
math: true
---

```haskell
calc :: String -> Float
calc expr =
    case [(calc num1) `op` (calc num2) | (op, opName) <- op's, let res = splitPoint opName, not $ null res, let (num1, num2) = head res] of
        c:_ -> c; _ -> matchFunc
    where
        inParenth = scanl (+) 0 $ map (\ch -> case ch of '(' -> 1; ')' -> -1; otherwise -> 0) expr
        splitPoint opName = [(take i expr, drop (i+1) expr) | (i,ch) <- zip [0..] expr, ch == opName, inParenth !! i == 0]
        op's = [((+), '+'), ((-), '-'), ((*), '*'), ((/), '/'), ((**), '^')]
        func's = [(id, "("), (tan, "tan("), (cos, "cos("), (sin, "sin("), (exp, "exp("), (log, "log("), (sqrt, "sqrt(")]
        matchFunc = case [func $ calc $ drop len $ init expr | (func, funcName) <- func's, let len = length funcName, take len expr == funcName] of
            c:_ -> c; _ -> toValue expr
        toValue str = case str of "pi" -> pi; "e" -> (exp 1); _ -> read str :: Float

```

支持 `+` `-` `*` `/` `^` 运算符以及 `tan` `cos` `sin` `exp` `log` `sqrt` 等常用函数。

```plaintext
ghci> calc "(45*(cos(25)+tan(255-2^5))+22*5)*152-cos(44+255)*23.4+22-(22+3)*14.6"
22813.395
```