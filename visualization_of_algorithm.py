import main_file_with_time_diff as algo
import matplotlib.pyplot as plt
import pickle


#### Dumping stats into file
# random_12 = [103723971119,118233435679,655373525717,701234567897,553559562581,619737131179,308457624821,454280348267,999999000001,293826343073]
# time_stat = []
# for prime in random_12:
#     time = algo.check_prime(prime)
#     print(time)
#     time_stat.append(time)
#
# with open('Stats_of_time_taken_12.pickle','wb') as file:
#     pickle.dump((time_stat,random_12),file)


####Loading stats from file
loaded_stat = pickle.load(open('Stats_of_time_taken_12.pickle','rb'))
time_stat , random_12 = loaded_stat
plt.scatter(random_12,time_stat)
plt.show()