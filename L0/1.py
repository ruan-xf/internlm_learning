import sys  
  
# 你要添加的目录路径  
your_directory = '/root/myenvs'  
  
# 检查该目录是否已经在 sys.path 中  
if your_directory not in sys.path:  
    # 将目录添加到 sys.path  
    sys.path.append(your_directory)  
  
# 现在你可以直接导入该目录中的模块了  
# 例如：import your_module
import numpy as np
print(np.__version__)
print(np.random.random(5))