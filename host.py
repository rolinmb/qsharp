from qubit import *

import matplotlib.pyplot as plt
import time

def compare_randoms(batch_num, n_iters):
    print(f"\t<BATCH *{batch_num}* RANDOMS PERFOMANCE>")
    main_ones = 0
    numpy_ones = 0
    qsharp_ones = 0
    for i in range(0, n_iters):
        obs_main = int(round(get_true_random(), 0))
        obs_numpy = numpy_random_bit()
        obs_qsharp = qsharp_random_bit()
        if obs_main == 1:
            main_ones += 1
        if obs_numpy == 1:
            numpy_ones += 1
        if obs_qsharp == 1:
            qsharp_ones += 1

    print(f"""\t    > get_true_random() 1s: {main_ones}
            > Numpy 1s: {numpy_ones}
            > Q# 1s: {qsharp_ones}""")

def run_qubits_test(n_batches, n_iters):
    print(f"\n|QUBITS TESTING : n_batches = {n_batches}, n_iters per batch = {n_iters}|")
    try: # non-classical / superimposed quantums states
        q0 = qubit(1+0j, 0+0j) # |0>
        q1 = qubit(0+0j, 1+0j) # |1>
        q2 = qubit(1/np.sqrt(2)+0j, 1/np.sqrt(2)+0j)
        q3 = qubit(1/np.sqrt(2)+0j, -1/np.sqrt(2)+0j)
        q4 = qubit(1/2+0j, np.sqrt(3)/2+0j)
        q5 = qubit(-1/np.sqrt(3)+0j, np.sqrt(2)/np.sqrt(3)+0j)
        q6 = qubit(1/np.sqrt(10)+0j, np.sqrt(9)/np.sqrt(10)+0j)
    except Exception as e:
        print(e)

    q0_ones = 0
    q1_ones = 0
    q2_ones = 0
    q3_ones = 0
    q4_ones = 0
    q5_ones = 0
    q6_ones = 0
    # simulating many coinflips, different qbits have different probabilities for 1
    for j in range(0, n_batches): # n_batches simulations/batches
        print(f"[TEST BATCH *{j+1}*]")
        q0_ones = 0
        q1_ones = 0
        q2_ones = 0
        q3_ones = 0
        q4_ones = 0
        q5_ones = 0
        q6_ones = 0
        for i in range(0, n_iters): # take n_iterations measurments per batch
            q0_obs = q0.measure()
            q1_obs = q1.measure()
            q2_obs = q2.measure()
            q3_obs = q3.measure()
            q4_obs = q4.measure()
            q5_obs = q5.measure()
            q6_obs = q6.measure()
            if q0_obs == 1:
                q0_ones += 1
            if q1_obs == 1:
                q1_ones += 1
            if q2_obs == 1:
                q2_ones += 1
            if q3_obs == 1:
                q3_ones += 1
            if q4_obs == 1:
                q4_ones += 1
            if q5_obs == 1:
                q5_ones += 1
            if q6_obs == 1:
                q6_ones += 1

        print(f"\t[BATCH *{j+1}* RESULTS]")
        print(f"\t->Total 1s observed from q0 {q0}: {q0_ones}") # 100% chance collapses to 0
        print(f"\t->Total 1s observed from q1 {q1}: {q1_ones}") # 100% chance collapses to 1
        print(f"\t->Total 1s observed from q2 {q2}: {q2_ones}") # 50% chance to collapse to 0 or 1
        print(f"\t->Total 1s observed from q3 {q3}: {q3_ones}") # 50% chance to collapse to 0 or 1
        print(f"\t->Total 1s observed from q4 {q4}: {q4_ones}") # 25% chance to collapse to 0; 75% chance to collapse 1
        print(f"\t->Total 1s observed from q5 {q5}: {q5_ones}") # 33.333% chance to collapse to 0; 66.666% chance to collapse to 1
        print(f"\t->Total 1s observed from q6 {q6}: {q6_ones}") # 10% chance to collapse to 0; 90% chance to collapse to 1
        compare_randoms(j+1, n_iters)
        
if __name__ == '__main__':
    start = time.time()
    n_batches = 50
    n_iters = 1000
    run_qubits_test(n_batches, n_iters)
    '''
    try:
        q0 = qubit(1, 0) # |0> Classical 1 & 0
        q1 = qubit(0, 1) # |1>
        q2 = qubit(1/np.sqrt(2), 1/np.sqrt(2)) # superimposed qubit examples
        q3 = qubit(1/np.sqrt(2), -1/np.sqrt(2))
        q4 = qubit(1/2, np.sqrt(3)/2)
        q5 = qubit(-1/np.sqrt(3), np.sqrt(2)/np.sqrt(3))
        q6 = qubit(1/np.sqrt(10), np.sqrt(9)/np.sqrt(10))
    except Exception as e:
        print(e)
    
    # plotting qubits on 3D Bloch Sphere
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    fig.suptitle('Bloch Sphere')
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    r = 0.05
    u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r)
    ax.scatter([0], [0], [1], color="k", s=50)
    ax.scatter([0], [0], [-1], color="k", s=50)
    qcoords = q2.get_bloch_coords()
    ax.scatter(qcoords[0], qcoords[1], qcoords[2], color="b", s=100)
    plt.show()
    '''
    print(f"Total Excution Time: {round(time.time() - start, 2)} seconds")