import json, math, sys
d = sys.argv[1]
K = 111.32; C = math.cos(math.radians(48.7)); LON0 = 16.75; LAT0 = 49.68
def P(lon, lat): return ((lon-LON0)*C*K, (LAT0-lat)*K)
ring = json.load(open(d+'/svk10m.json'))['coordinates'][0]
pr = [P(*p) for p in ring]
xs=[p[0] for p in pr]; ys=[p[1] for p in pr]
print('bounds', min(xs), max(xs), min(ys), max(ys), file=sys.stderr)
border = 'M' + 'L'.join(f'{x:.1f},{y:.1f}' for x,y in pr) + 'Z'
def inside(x,y):
    c=False
    for (x1,y1),(x2,y2) in zip(pr, pr[1:]+pr[:1]):
        if (y1>y)!=(y2>y) and x < (x2-x1)*(y-y1)/(y2-y1)+x1: c=not c
    return c
def dseg(px,py,a,b):
    (x1,y1),(x2,y2)=a,b; dx,dy=x2-x1,y2-y1; L=dx*dx+dy*dy
    t=0 if L==0 else max(0,min(1,((px-x1)*dx+(py-y1)*dy)/L))
    return math.hypot(px-x1-t*dx, py-y1-t*dy)
def near(x,y,tol=2.5):
    return inside(x,y) or min(dseg(x,y,a,b) for a,b in zip(pr,pr[1:]+pr[:1]))<tol
want={'Danube','Donau','Morava','Váh','Hron','Hornád','Ipel','Dunajec','Slana','Latorytsya'}
paths=[]
for fn in ['rivers.geojson','riverseu.geojson']:
    for f in json.load(open(d+'/'+fn))['features']:
        g=f['geometry']; n=f['properties'].get('name')
        if not g or n not in want: continue
        lines=[g['coordinates']] if g['type']=='LineString' else g['coordinates']
        for l in lines:
            cur=[]
            for pt in l:
                x,y=P(pt[0],pt[1])
                if near(x,y): cur.append((x,y))
                else:
                    if len(cur)>1: paths.append(cur)
                    cur=[]
            if len(cur)>1: paths.append(cur)
rivers=''.join('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in c) for c in paths)
json.dump({'border':border,'rivers':rivers,'w':max(xs),'h':max(ys)}, open(d+'/geo_out.json','w'))
print(len(border), len(rivers), file=sys.stderr)
