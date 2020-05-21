
def solution(s, n):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    uppercase= alpha.upper()

    for j in range(len(s)):
        if s[j] in uppercase:
# 대문자에 있는 문자열에 있으면 그 알파벳이 있는 위치를 저장
# 그 알파벳이 있는 위치를 저장
            original = uppercase.find(s[j])
            Caesar = (original + n) % 26
            answer += uppercase[Caesar]
        if s[j] in alpha:
            original = alpha.find(s[j])
            Caesar = (original + n) % 26
            answer += alpha[Caesar]
        if s[j] == " ":
            answer += " "
    return answer