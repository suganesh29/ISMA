
import numpy as np
from tabulate import tabulate


RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}

print("Enter the no of Criteria")
n = int(input())

print("Enter the values row wise:")
A_arr = []
while not A_arr or len(A_arr) < len(A_arr[0]):
    A_arr.append(list(map(float, input().split())))
#print(A_arr)
#print(type(A_arr))



def main():
   
    PWmatrix = np.array(A_arr)
    SizeA_arr=PWmatrix.shape[0]
    print('Pair-Wise Matrix:')
    
	
    print(tabulate(PWmatrix , tablefmt="simple", floatfmt = ".4f"))
    print("\n")
    PWmatrix_sum0 = PWmatrix.sum(axis=0) # column sum
    NorPWmatrix = PWmatrix / PWmatrix_sum0  
    print('Normalized Pair- wise  matrix:')
    print(tabulate(NorPWmatrix , tablefmt="simple", floatfmt = ".4f"))
   
    NorPWmatrixRowsum = NorPWmatrix.sum(axis=1)
    #print(NorPWmatrixRowsum)
    #print("\n")
    #b_sumPrint=np.around(b_sum,4)
    #print('Weighted Sum : %s' % b_sumPrint)
    #print("\n")
    
   # W = NorPWmatrixRowsum.sum()
    #for w in NorPWmatrixRowsum:
        #w_arr.append(w/W)
    CriteriaWeight_arr = []
    CriteriaWeight_arr= NorPWmatrixRowsum/ SizeA_arr
    
   
 
    CriteriaWeight_arrPrint=np.around(CriteriaWeight_arr,4)
    print('Criteria weights:%s' % CriteriaWeight_arrPrint )
    print("\n")
   

    AW = []
    for a in PWmatrix :
        aa = a * CriteriaWeight_arr
        AW.append(aa.sum())
        AWPrint=np.around(AW,4)
    print('Weighted Sum is: %s' % AWPrint)
    print("\n\n")

    result = np.array(AW) / np.array(CriteriaWeight_arr)
    res= np.around(result,4)
    print('λ Values : %s' % res)
    print("\n")

    row = result.shape[0]
    Max = result.sum()/row
    MaxPrint= np.around(Max,4)
    print('λMax: %s' % MaxPrint)
    print("\n")

    CI = (Max - row) / (row - 1)
    CIPrint= np.around(CI,4)
    print('CI: %s' % CIPrint)
    print("\n")
    
    CR = CI / RI_dict[row]
    CRPrint= np.around(CR,4)
    print('CR: %s' % CRPrint)
    
 
if __name__ == '__main__':
    main()








'''from sympy import * 
init_printing()
import sympy
print(sympy.__version__)


eval_mat_1 = Matrix(    
    [[1   , 3,],
     [1/3 , 1]]
)
eigen_val_vects_1 = eval_mat_1.eigenvects()
#print(eigen_val_vects_1)
EIGEN_VAL_IDX = 0
MULUTIPLICITY_IDX = 1
EIGEN_VEC_IDX = 2
max(eigen_val_vects_1, key=(lambda x: x[EIGEN_VAL_IDX]))
eigen_val, multiplicity, eigen_vec = max(eigen_val_vects_1, key=(lambda x: x[EIGEN_VAL_IDX]))
#print(eigen_vec)
type(eigen_vec)
eigen_vec[0]
type(eigen_vec[0])
print(eigen_vec[0] / sum(eigen_vec[0]))

def calc_ahp_weight_vec(comparison_mat):
    
    比較行列から重みベクトルを計算する関数

    Arguments:

    comparison_mat -- 比較行列
    
    
    
    # 固有値のインデックス
    EIGEN_VAL_IDX = 0
    
    # sympyの関数を使って、固有値と固有ベクトルを得る
    eigen_val_vects = comparison_mat.eigenvects()
    
    # 最大固有値とその時の多重度・固有ベクトルを取得
    eigen_val, multiplicity, eigen_vec = max(eigen_val_vects, key=(lambda x: x[EIGEN_VAL_IDX]))
    
    # 重みの合計が1になるように標準化
    weight_vec = eigen_vec[0] / sum(eigen_vec[0])
    
    # 重みを返す
    return(weight_vec)
    calc_ahp_weight_vec(eval_mat_1)
    eval_mat_1 = Matrix(    
    [[1   , 3,],
     [1/3 , 1]]
)

# 味に関する、お寿司と牛丼の比較行列
# 要素1がお寿司
# 要素2が牛丼
taste_mat_1 = Matrix(    
    [[1   , 5,],
     [1/5 , 1]]
)

# 価格に関する、お寿司と牛丼の比較行列
# 要素1がお寿司
# 要素2が牛丼
price_mat_1 = Matrix(    
    [[1 , 1/9,],
     [9 ,   1]]
)
eval_weight_1 = calc_ahp_weight_vec(eval_mat_1)
#print(eval_weight_1)
taste_weight_1 = calc_ahp_weight_vec(taste_mat_1)
N(taste_weight_1, 2)
price_weight_1 = calc_ahp_weight_vec(price_mat_1)
join_mat_1 = taste_weight_1.row_join(price_weight_1)
N(join_mat_1, 2)
#print(price_weight_1)

#print(join_mat_1 * eval_weight_1)


eval_mat_2 = Matrix(    
    [[1   , 3  , 15],
     [1/3 , 1  , 5],
     [1/15, 1/5, 1]]
)
eigen_val_vects_2 = eval_mat_2.eigenvects()
max(eigen_val_vects_2, key=(lambda x: x[EIGEN_VAL_IDX]))
eval_weight_2 = calc_ahp_weight_vec(eval_mat_2)
N(eval_weight_2, 2)
eval_mat_3 = Matrix(    
    [[1   , 3  , 1],
     [1/3 , 1  , 5],
     [1   , 1/5, 1]]
)
eigen_val_vects_3 = eval_mat_3.eigenvects()
#print(eigen_val_vects_3)
eigen_val_vects_3[0][EIGEN_VAL_IDX]


eigen_val_vects_3[0][EIGEN_VAL_IDX].as_real_imag()



eigen_val_vects_3[0][EIGEN_VAL_IDX].as_real_imag()[0]


max(eigen_val_vects_3, key=(lambda x: x[EIGEN_VAL_IDX].as_real_imag()[0]))

eval_mat_3.shape


n = eval_mat_3.shape[0]
max_eigen_val = max(eigen_val_vects_3, key=(lambda x: x[EIGEN_VAL_IDX].as_real_imag()[EIGEN_VAL_IDX]))[EIGEN_VAL_IDX]
ci = (max_eigen_val - n) / (n - 1)
print(ci)


ri = {3:0.52,
      4:0.89,
      5:1.11,
      6:1.25,
      7:1.35,
      8:1.40,
      9:1.45,
      10:1.49
     }

cr = ci / ri[n]
cr


def calc_ahp_weight_vec_over3(comparison_mat):
    
    比較行列から重みベクトルを計算する関数
    一貫性の評価のための指標CIとCRも併せて算出して表示させる
    
    比較対象が3つ以上の時のみ使用できる

    Arguments:

    comparison_mat -- 比較行列
    
    
    # 固有値のインデックス
    EIGEN_VAL_IDX = 0
    
    # sympyの関数を使って、固有値と固有ベクトルを得る
    eigen_val_vects = comparison_mat.eigenvects()
    
    # 最大固有値とその時の固有ベクトルを取得
    # 固有値の大小は、実数部で評価
    eigen_val, multiplicity, eigen_vec = max(eigen_val_vects, key=(lambda x: x[EIGEN_VAL_IDX].as_real_imag()))
    
    # 計算過程を出力
    print("================================================================================")

    # ランダム指標(初出はSaaty（2013）：
    # 『Theory and Applications of the Analytic Network Process: Decision Making With Benefits, Opportunities, Costs, and Risks』)
    ri = {3:0.52,
          4:0.89,
          5:1.11,
          6:1.25,
          7:1.35,
          8:1.40,
          9:1.45,
          10:1.49
         }
    
    # 一貫性指標の計算
    n = comparison_mat.shape[0]
    ci = (eigen_val - n) / (n - 1)
    cr = ci / ri[n]

    print("一Evaluation of consistency. If CI>0.1 (or CI>0.15), fix the comparison matrix")
    print("Number of comparison targets　：", n)
    print("Maximum eigenvalue :", N(eigen_val, 2))
    print("Index of consistency CI：", N(ci, 2))
    print("Persistence index CR：", N(cr, 2))
    
    print("================================================================================")
    
    # 重みの合計が1になるように標準化
    weight_vec = eigen_vec[0] / sum(eigen_vec[0])
    
    # 重みを返す
    return(weight_vec)



eval_weight_3 = calc_ahp_weight_vec_over3(eval_mat_3)
N(eval_weight_3, 2)


eval_mat_4 = Matrix(    
    [[1  , 3,    2],
     [1/3, 1,    1/2],
     [1/2, 2,    1]]
)

# 味に関する、お寿司と牛丼、ラーメンの比較行列
# 要素1がお寿司
# 要素2が牛丼
# 要素3がラーメン
taste_mat_4 = Matrix(    
    [[1  , 3,  2  ],
     [1/3, 1,  1/3],
     [1/2, 3,  1  ]]
)

# 価格に関する、お寿司と牛丼の比較行列
# 要素1がお寿司
# 要素2が牛丼
# 要素3がラーメン
price_mat_4 = Matrix(    
    [[1  , 1/9, 1/5],
     [9  , 1,   3  ],
     [5  , 1/3, 1  ]]
)

# 待ち時間に関する、お寿司と牛丼の比較行列
# 要素1がお寿司
# 要素2が牛丼
# 要素3がラーメン
time_mat_4 = Matrix(    
    [[1  , 1/9, 1/9],
     [9  , 1,   1  ],
     [9  , 1,   1  ]]
)



eval_weight_4 = calc_ahp_weight_vec_over3(eval_mat_4)
N(eval_weight_4, 2)

taste_weight_4 = calc_ahp_weight_vec_over3(taste_mat_4)
N(taste_weight_4, 2)

price_weight_4 = calc_ahp_weight_vec_over3(price_mat_4)
N(price_weight_4, 2)



time_weight_4 = calc_ahp_weight_vec_over3(time_mat_4)
N(time_weight_4, 2)


join_mat_4 = taste_weight_4.row_join(price_weight_4).row_join(time_weight_4)
N(join_mat_4, 2)



N(join_mat_4 * eval_weight_4, 2)


























import numpy as np

#Change according to the problem
importance = np.array([[1, 1 / 3, 1, 1 / 5, 2, 3],  #Here enter the construction matrix
                       [3, 1, 2, 1 / 5, 3, 4],
                       [1, 1 / 2, 1, 1 / 4, 3, 2],
                       [5, 5, 4, 1, 5, 6],
                       [1 / 2, 1 / 3, 1 / 3, 1 / 5, 1, 1 / 3],
                       [1 / 3, 1 / 4, 1 / 2, 1 / 6, 3, 1]])
column_sum = np.sum(importance, 0)
importance /= column_sum
row_sum = np.sum(importance, 1)
w = row_sum / np.sum(row_sum)
print(w)





import numpy as np
import pandas as pd
import warnings


class AHP:
    def __init__(self, criteria, b):
        self.RI = (0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49)
        self.criteria = criteria
        self.b = b
        self.num_criteria = criteria.shape[0]
        self.num_project = b[0].shape[0]

    def cal_weights(self, input_matrix):
        input_matrix = np.array(input_matrix)
        n, n1 = input_matrix.shape
        assert n == n1, 'Not a square matrix'
        for i in range(n):
            for j in range(n):
                if np.abs(input_matrix[i, j] * input_matrix[j, i] - 1) > 1e-7:
                    raise ValueError('Not an anti-symmetric matrix')

        eigenvalues, eigenvectors = np.linalg.eig(input_matrix)

        max_idx = np.argmax(eigenvalues)
        max_eigen = eigenvalues[max_idx].real
        eigen = eigenvectors[:, max_idx].real
        eigen = eigen / eigen.sum()

        if n > 9:
            CR = None
            warnings.warn('Unable to judge consistency')
        else:
            CI = (max_eigen - n) / (n - 1)
            CR = CI / self.RI[n]
        return max_eigen, CR, eigen

    def run(self):
        max_eigen, CR, criteria_eigen = self.cal_weights(self.criteria)
        #print('Criteria layer: Maximum eigenvalue {:<5f}, CR={:<5f}, test {}passed.format(max_eigen, CR, '' if CR < 0.1 else 'Do not')
        print('Criteria layer weight={}\n'.format(criteria_eigen))

        max_eigen_list, CR_list, eigen_list = [], [], []
        for i in self.b:
            max_eigen, CR, eigen = self.cal_weights(i)
            max_eigen_list.append(max_eigen)
            CR_list.append(CR)
            eigen_list.append(eigen)

        pd_print = pd.DataFrame(eigen_list,
                                index=['Guidelines' + str(i) for i in range(self.num_criteria)],
                                columns=['Program' + str(i) for i in range(self.num_project)],
                                )
        pd_print.loc[:, 'Maximum eigenvalue'] = max_eigen_list
        pd_print.loc[:, 'CR'] = CR_list
        pd_print.loc[:, 'Consistency check'] = pd_print.loc[:, 'CR'] < 0.1
        print('Scheme layer')
        print(pd_print)

        # Target layer
        obj = np.dot(criteria_eigen.reshape(1, -1), np.array(eigen_list))
        print('\nTarget layer', obj)
        print('The best choice is the plan{}'.format(np.argmax(obj)))
        return obj


if __name__ == '__main__':
    # Criteria importance matrix
    criteria = np.array([[1, 2, 7, 5, 5],
                         [1 / 2, 1, 4, 3, 3],
                         [1 / 7, 1 / 4, 1, 1 / 2, 1 / 3],
                         [1 / 5, 1 / 3, 2, 1, 1],
                         [1 / 5, 1 / 3, 3, 1, 1]])

    # For each criterion, the priority of the program
    b1 = np.array([[1, 1 / 3, 1 / 8], [3, 1, 1 / 3], [8, 3, 1]])
    b2 = np.array([[1, 2, 5], [1 / 2, 1, 2], [1 / 5, 1 / 2, 1]])
    b3 = np.array([[1, 1, 3], [1, 1, 3], [1 / 3, 1 / 3, 1]])
    b4 = np.array([[1, 3, 4], [1 / 3, 1, 1], [1 / 4, 1, 1]])
    b5 = np.array([[1, 4, 1 / 2], [1 / 4, 1, 1 / 4], [2, 4, 1]])

    b = [b1, b2, b3, b4, b5]
    a = AHP(criteria, b).run()'''
