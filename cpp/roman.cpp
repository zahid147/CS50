class Solution {
public:
    int romanToInt(string s) {
        int T = s.size(), sum = 0, i = 0;
        while(T){

            if(s[i] == 'V'){
                sum += 5;
                T--, i++;
            }
            else if(s[i] == 'L'){
                sum += 50;
                T--, i++;
            }
            else if(s[i] == 'D'){
                sum += 500;
                T--, i++;
            }
            else if(s[i] == 'M'){
                sum += 1000;
                T--, i++;
            }

            else if(s[i] == 'I'){
                if(s[i+1] == 'V'){
                    sum += 4;
                    T -= 2, i += 2;
                }
                else if(s[i+1] == 'X'){
                    sum += 9;
                    T -= 2, i += 2;
                }
                else{
                    sum += 1;
                    T--, i++;
                }
            }

            else if(s[i] == 'X'){
                if(s[i+1] == 'L'){
                    sum += 40;
                    T -= 2, i += 2;
                }
                else if(s[i+1] == 'C'){
                    sum += 90;
                    T -= 2, i += 2;
                }
                else{
                    sum += 10;
                    T--, i++;
                }
            }

            else if(s[i] == 'C'){
                if(s[i+1] == 'D'){
                    sum += 400;
                    T -= 2, i += 2;
                }
                else if(s[i+1] == 'M'){
                    sum += 900;
                    T -= 2, i += 2;
                }
                else{
                    sum += 100;
                    T--, i++;
                }
            }
        }
        return sum;
    }
};
