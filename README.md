#### 8.2.7 OEC/OEC-Turbo 的安装方法
- 下载 [RKDevTool](https://github.com/ophub/kernel/releases/download/tools/FastRhino_r68s_RKDevTool_Release_v2.86___DriverAssitant_v5.1.1.tar.gz) 工具及驱动，解压并安装 DriverAssitant 驱动程序，打开 RKDevTool 工具。(注意，请使用2.84版本工具而不是2.86，2.86版本无法写入全盘镜像)
- 下载 [OEC/OEC-Turbo Base]并解压。
##### 8.2.7.1 能够进入SSH后台
- OEC/OEC-Turbo 如果能够进入原厂SSH镜像后台，可以免拆刷入。
- 电脑，盒子均不要联网，reset OEC/OEC-Turbo，用网线直接连接盒子与电脑，修改电脑IP为：10.9.8.x（如10.9.8.8），登录ssh后台（IP：10.9.8.7，用户名root,密码SN后四位+rk35662019）
- 在进入SSH后台后,使用fw_setenv xl_softmode "factory" 设置bootloader模式。
- 断开电源，长按RESET键，用Type-C线连接电脑，工具提示`发现一个 LOADER 设备`。
- 右键表格栏，选择添加项，地址输入0x00000000,路径选择解压出来的[OEC/OEC-Turbo Base]。刷入镜像，等待完成。
<div style="width:100%;margin-top:40px;margin:5px;">
<img src=https://github.com/user-attachments/assets/2ff25684-7a71-4c5d-8b2d-59c9d118194d width="600" /><br />
</div>
- 将镜像写入U盘，插入OEC/OEC-Turbo，开机会自动启动到armbian。
- 使用`oec-install-emmc`命令安装进eMMC.
#### 8.2.7.2 不能进入SSH后台
-如果不能进入SSH后台，则需要拆机短接.
- 拆机短接图示触点,上电，等待约2-3秒，电脑提示`发现一个 MASKROM 设备`。
<div style="width:100%;margin-top:40px;margin:5px;">
<img src=https://github.com/user-attachments/assets/2381520a-cb2a-4599-8d21-5b0bad7ec93f width="600" /><br />
</div>
#### 8.2.7.2.1 直接线刷
- 修改第一项 地址 `0xCCCCCCCC`,文件选择`MiniLoaderAll.bin`。
- 右键表格栏，选择添加项，地址 0x00000000, 名字 system, 路径选择要刷的 Armbian.img 系统。点击执行，等待进度条完成即可
#### 8.2.7.2.2 u盘写入
- 右键表格栏，选择添加项，地址输入0x00000000,路径选择解压出来的[OEC/OEC-Turbo Base]。刷入镜像，等待完成。
<div style="width:100%;margin-top:40px;margin:5px;">
<img src=https://github.com/user-attachments/assets/33bc678e-c858-42e4-a85a-a1af9310dd20 width="600" /><br />
</div>
- 将镜像写入U盘，插入OEC/OEC-Turbo，开机会自动启动到armbian。
- 使用`oec-install-emmc`命令安装进eMMC.
