linguagens = ["python","java", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x))) # ['c', 'js', 'java', 'java', 'python', 'csharp']
print(sorted(linguagens, key=lambda x:len(x), reverse=True)) #['python', 'csharp', 'java', 'java', 'js', 'c']