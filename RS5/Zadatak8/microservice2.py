'''
Drugi mikroservis cat_fact_check mora slušati na portu 8087 i na endopintu /facts očekivati JSON
objekt s listom činjenica o mačkama u tijelu HTTP zahtjeva. Glavna dužnost ovog mikroservisa je da provjeri
svaku činjenicu sadrži li riječ cat ili cats , neovisno o velikim i malim slovima. Odgovor neka bude JSON
objekt s novom listom činjenica koje zadovoljavaju prethodni uvjet.
'''



from aiohttp import web
import re


def filter_facts(facts):
    """Filter facts containing 'cat' or 'cats'."""
    return [fact for fact in facts if re.search(r'\bcat(s)?\b', fact, re.IGNORECASE)]


async def fact_check(request):
    """Check facts and return only those that match the condition."""
    try:
        data = await request.json()
        facts = data.get('facts', [])
        filtered_facts = filter_facts(facts)
        return web.json_response({"filtered_facts": filtered_facts})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)


app = web.Application()
app.router.add_post('/facts', fact_check)

if __name__ == '__main__':
    web.run_app(app, port=8087)
