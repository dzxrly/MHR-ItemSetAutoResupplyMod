<div align="center">

# MHR Item set Auto Resupply Mod

</div>

<div align="center">

![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdzxrly%2FMHR-ItemSetAutoResupplyMod%2Fmain%2Fversion.json&query=%24.version&style=for-the-badge&label=VERSION) [![GitHub License](https://img.shields.io/github/license/dzxrly/MHR-ItemSetAutoResupplyMod?style=for-the-badge)](https://github.com/dzxrly/MHR-ItemSetAutoResupplyMod/blob/main/LICENSE) [![Static Badge](https://img.shields.io/badge/Nexusmods-Auto%20Resupply%20Item%20Set-%23d28934?style=for-the-badge)](https://www.nexusmods.com/monsterhunterrise/mods/1088)

</div>

A mod of Monster Hunter Rise (SunBreak) for resupply item set when quest finished automatically. / 用于怪物猎人崛起（含曙光）的任务完成时自动加载预设的个人道具组合Mod。

---

## Requirements:
- [REFramework](https://www.nexusmods.com/monsterhunterrise/mods/26)
- [REFramework D2D](https://www.nexusmods.com/monsterhunterrise/mods/134)

## How To Install:
1. Install REFramework and REFramework D2D;
2. Download the mod;
3. Unzip the mod to the Monster Hunter Rise root directory. So the final directory seems like ./reframework/autorun/itemSetAutoResupply.lua.

## How To Use:
- First Use:  (1) Open REFramework menu and unfold the Script Generated UI menu item. You will find the Item Set Auto Resupply window. (2) Click the Reload Item Set List button to read your item set list. (3) Select an item set you want to use then there is a tip "Item Set Has Been Set To [xxx]" below. It means your selection has been saved and the mod is working!
- No First Use: When you select your item set following the above steps, you don't need to do any more operations, the mod will work automatically.

---

## 前置：
- [REFramework](https://www.nexusmods.com/monsterhunterrise/mods/26)
- [REFramework D2D](https://www.nexusmods.com/monsterhunterrise/mods/134)

## 安装方式：
1. 安装REFramework和REFramework D2D；
2. 下载MOD；
3. 将MOD解压缩后存放至Monster Hunter Rise根目录，即./reframework/autorun/itemSetAutoResupply.lua。

## 如何使用：
- 首次使用：（1）打开REFramework菜单并且点击Script Generated UI，此时会打开一个新的窗口叫做Item Set Auto Resupply。（2）点击Reload Item Set List按钮读取已保存的道具个人组合。（3）在下拉框中选择一个你想要的道具组合，此时下拉框下方会显示“Item Set Has Been Set To [xxx]”，表明MOD已经设置成功！
- 后续使用：因为已按照上述步骤设置完成，因此后续不需要做任何操作，MOD即可自动运行。

---

## Update:

### Ver1.4 - FEATURE UPDATE:
1. Update Chinese fonts support. / 更新了中文支持。

### Ver1.3 - FEATURE UPDATE:
1. In this version, item set load tip and item NOT ENOUGH tip will show in the game. [New Additional Requirements: REFramework D2D] / 添加了游戏内显示个人组合已自动加载和个人组合物品不足的提示。【需要安装新的依赖库：REFramework D2D】
To open the feature above, you should open the REFramework menu and click the Script Generated UI, then check two SHOW BUTTONs! / 开启上述功能需要打开REF菜单然后点击Script Generated UI，再勾选两个带有Show字样的按钮。

### Ver1.2 - BUG FIX:
1. Fix a bug that makes REF UI start flickering in the Training Area, thx for @bbacmk's reporting. / 修复了一个在训练场中使用MOD时导致REF UI闪屏的BUG。
PS: Please DO NOT click the Reload Item Set List button in the Training Area, it will cause the options in the dropmenu to disappear. / 请尽量不要在训练场中点击Reload Item Set List按钮，会导致下拉菜单内容消失。

### Ver1.1 - BUG FIX:
1. Fix a bug that makes your selection locked on the first item set, caused by the converter of String & Integer & Float. / 修复了一个会导致个人组合被锁定在第一套的BUG，应该是因为隐式类型转换导致的。
