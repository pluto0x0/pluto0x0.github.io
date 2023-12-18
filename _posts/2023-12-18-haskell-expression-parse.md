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
        func's = [(id, "("), (tan, "tan("), (cos, "cos("), (sin, "sin("), (exp, "exp("), (log, "log(")]
        matchFunc = case [func $ calc $ drop (length funcName) $ init expr | (func, funcName) <- func's, take (length funcName) expr == funcName] of
            c:_ -> c; _ -> toValue expr
        toValue str = case str of "pi" -> pi; "e" -> (exp 1); _ -> read str :: Float
```

支持 `+` `-` `*` `/` 运算符以及 `tan` `cos` `sin` `exp` `log` 等常用函数。
