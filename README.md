# 演算法

1. 雙方 Check 自己的 Nat 類型，至少要有一方為 Cone Nat Side(作為 Server 方)
2. Server 方建立一個 UDP Server 等待連線。
3. Symmetric Nat 為 Client 發起 UDP 連線到剛剛的 Cone Side Server 方。
4. 這樣 Nat 的 UDP Hole Punching 就完成了。
5. 接下來只要 Server 方收到 Client 的 Message 在用 sock 物件將資訊 send 回去 Client 端的 IP:Port。
6. 兩邊完成 P2P UDP 連線。
