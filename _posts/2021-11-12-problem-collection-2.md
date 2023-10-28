# 1580C

对于所有 $x_i+y_i>\sqrt{m}$ 的火车，每次add/remove用差分数组暴力维护。单次修改复杂度 $O(\sqrt m)$ ，对于 $x_i+y_i < \sqrt m$ 的火车，其 $x_i+y_i$ 值的种类不超过 $\sqrt m$， 每次取模即可。

