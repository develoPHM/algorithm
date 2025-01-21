cacheSize = 3
cities = ["a", "b", "a", "c", "d", "a"]
cache = []
ans = 0
if cacheSize == 0:
    ans += len(cities) * 5
else:
    for c in cities:
        c = c.lower()
        if len(cache) < cacheSize:
            if c in cache:
                ans += 1
                cache.remove(c)
                cache.append(c)
                continue
            cache.append(c)
            ans += 5
            continue
        if c in cache:
            cache.remove(c)
            ans += 1
            cache.append(c)
        else:
            cache.pop(0)
            cache.append(c)
            ans += 5
print(ans)