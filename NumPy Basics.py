{
 "cells": [
  {
   "cell_type": "raw",
   "id": "7dbae479-f17e-4627-9540-f728a3f7fbf0",
   "metadata": {},
   "source": [
    "One dimensional num py array are same as tuples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a19e7dde-7dca-40b4-9b16-520aeb587822",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([[24,22,26,27,28]])  #way of storing is also same [] brackets are used to confirm they are array\n",
    "print(a[0,2]) #way of printing array elements is also same the only diffrence \n",
    "            #is 1st one is for dimension second number is for serial number in the dimension\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "09c4949e-0717-4706-a857-434d7aa26e4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[22 24 26 27 28]]\n"
     ]
    }
   ],
   "source": [
    "a.sort()  # Same like List U can also use sort nd other functions\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1eaae3a3-b8fc-4d5e-8f23-1add9656afbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[22 24 26 27 28]]\n"
     ]
    }
   ],
   "source": [
    "print(a[0:3])   # Same like list u can print other bunch of these"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc33971c-94bd-4f6e-98e5-e9f2a38d8b17",
   "metadata": {},
   "source": [
    "**Basic Function of Array**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ccdc81b6-afe8-4090-8ed1-523585d9e865",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int64')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.dtype         #It is used to get the type of array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1022b42c-73dd-4cab-94ef-3c0340145c5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 5)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.shape           #to get how much dimensions and objects are in array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c8213e31-263b-495f-913d-ad173b3910b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size           #To get the size of array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3ee3d0f1-50cb-472e-aa8c-e828a3407115",
   "metadata": {},
   "outputs": [],
   "source": [
    "rng = np.arange(99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2ecaf272-c521-4122-a2d1-4806c2a2817a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n",
       "       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,\n",
       "       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,\n",
       "       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rng"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9edb2f61-7445-4ea6-8afa-a90f955fc7be",
   "metadata": {},
   "source": [
    "**Zeros Ways To print Array**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6f4c6350-b41f-41a3-bf8e-b53659bca601",
   "metadata": {},
   "outputs": [],
   "source": [
    "zeros = np.zeros((2,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ef767557-edd6-4b43-8c94-5dd77a35783c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., 0., 0.],\n",
       "       [0., 0., 0., 0., 0.]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zeros"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "79ee84ee-6983-4971-b450-2d8398b84a05",
   "metadata": {},
   "outputs": [],
   "source": [
    "lspace = np.linspace(5,15,4)                  # It is used to get elements beetween to numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "400ccf90-4af1-43ae-991a-b47d08a9fc99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 5.        ,  8.33333333, 11.66666667, 15.        ])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lspace                                        # Format np.linspace(num1,num2 , elements u want)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "273c3325-a409-4097-9424-448fe4c5c59c",
   "metadata": {},
   "outputs": [],
   "source": [
    "rng = rng.reshape(3,33)        # Reshape is use to reshape the one dimensional arrays to \n",
    "                         # other dimensional arrays \n",
    "                         # Format is reshape(Dimensions, total numbers)\n",
    "                         # Multiple of dimensions , total number should be total elements in frist one\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "301ff220-f773-4e17-a3da-b8ed8328875a",
   "metadata": {},
   "outputs": [],
   "source": [
    "xis = [[10,12,13],[14,15,16],[17,18,19]]\n",
    "ar = np.array(xis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "01906731-aa05-4c83-b126-c212bd50e937",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[10, 12, 13],\n",
       "       [14, 15, 16],\n",
       "       [17, 18, 19]])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "02072752-c9c2-44e4-981c-7b7b63aeb5d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([41, 45, 48])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.sum(axis=0)       #axis 0 is the verticals elements of the numpy array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "cad94bc2-f931-4684-8728-66104d611025",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([35, 45, 54])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.sum(axis=1)       #axis 1 is the horizontals elements of the numpy array\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6d60aa4c-24e6-4b85-bd09-f672b30fef51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[10, 14, 17],\n",
       "       [12, 15, 18],\n",
       "       [13, 16, 19]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.T                  #It is used to tranform row into column nd vice versa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "64ef334e-50bc-4e3e-a91c-686077f31387",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "72"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.nbytes              #It tells How much bites are comsumed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "64cfb6f2-6a31-4c81-abb0-a5f4f23916b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.argmax()            #ArgMax is used to find Max element"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5bafa57a-270e-42d5-9c99-3233fc8135af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ar.argmin()           #ArgMin is used to find min element"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d227abb5-8e88-4813-9d51-806391b2429d",
   "metadata": {},
   "source": [
    "#Mathematical operation With NumPy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2b6a787f-5fb5-40cd-aaf5-d4db53d2d2ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "math1 = np.array([2,4,6,8,10])\n",
    "math2 = np.array([12,14,16,18,20])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4787a8b9-1fd1-4b17-b683-bcaf950c61c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([14, 18, 22, 26, 30])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math1+math2                   #You Can Add to array "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "edf76db3-fd58-429f-b38e-13c3b0f5dd38",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 24,  56,  96, 144, 200])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math1*math2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "14fbb05f-1869-4462-8516-6bdf16c0dd5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-10, -10, -10, -10, -10])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math1-math2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "22758c6e-6f24-4902-87cc-e901fa9627ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([6.        , 3.5       , 2.66666667, 2.25      , 2.        ])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math2/math1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "865dd730-aa99-479c-91fe-dfd6d2e82ec0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([2, 3, 4]),)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.where(math1>5)                     #Use to find the specific type of element\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99327015-4d15-4748-a6f1-ab3236e1d0db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
