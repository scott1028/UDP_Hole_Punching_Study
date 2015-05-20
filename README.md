# 演算法

1. 雙方 Check 自己的 Nat 類型，至少要有一方為 Cone Nat Side(作為 Server 方)
2. Server 方建立一個 UDP Server 等待連線。
3. Symmetric Nat 為 Client 發起 UDP 連線到剛剛的 Cone Side Server 方。

   Symmetric 端的 Client 要持續送 Empty Packets 或有資料的 Packet來保持 UDP Hole Punching 的維持時間
   因為起一個 Client 發出封包會戰本地端一個 Port，就是利用這個 Port 將資料收回來，所以要持續送資料 保持這個Port跟Nat伺服器的轉換通道暢通KeepAlive。

4. 這樣 Nat 的 UDP Hole Punching 就完成了。
5. 接下來只要 Server 方收到 Client 的 Message 在用 sock 物件將資訊 send 回去 Client 端的 IP:Port。
6. 當 Server 方知道 Client Nat Server 對應內部 Client 的 Port 時候, 直接關閉目前的 Server.py 用另一個 udp_client_B.py 用相同的 port 就可以把資料 Send 回去了。
7. 兩邊完成 P2P UDP 連線。

# 加入 Stun Server

* 用 stun server 來說就是雙方持續發送 UDP 封包給 Stun Server 保持 Nat Hole 轉換通道維持時間。然後雙方在各用對方的轉換 Port 將資料送給對方。
