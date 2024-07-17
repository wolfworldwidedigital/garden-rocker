import streamlit as st

html_content = """
<main class="container">
 <main class="container"> 
            <section class="category"> 
                <h2>Garden Webshops in the United Kingdom</h2> 
                <div class="description"> 
                    <p>
                        Discover the best online stores in the UK for all your gardening needs. From plants, seeds, and bulbs to garden tools, furniture, and accessories, these webshops offer a wide range of products to help you create and maintain your perfect garden.                 </p> 
                </div>                 
                <div class="websites"> 
                    <ul> 
                        <li><a href="https://www.horticentre.co.uk/">horticentre.co.uk</a>
                        </li>                         
                        <li><a href="https://www.provendernurseries.co.uk/">provendernurseries.co.uk</a>
                        </li>                         
                        <li><a href="https://www.barkukonline.co.uk/">barkukonline.co.uk</a>
                        </li>                         
                        <li><a href="https://www.gardenbuyer.co.uk/">Garden Centre Price Comparison</a>
                        </li>                         
                        <li><a href="https://www.cowellsgc.co.uk/">cowellsgc.co.uk</a>
                        </li>
                    </ul>                     
                </div>                 
            </section>             
            <section class="category"> 
                <h2>Garden Webshops in Ireland</h2> 
                <div class="description"> 
                    <p>
                        Discover Ireland's premier garden webshops, providing a diverse array of plants, gardening accessories, and outdoor furniture. Shop conveniently online and get expert advice to transform your garden into a lush, green oasis.


                    </p> 
                </div>                 
                <div class="websites"> 
                    <ul> 
                        <li><a href="https://www.jonesgc.com/">Jones Garden Centre</a>
                        </li>                         
                        <li><a href="https://www.hanleysofcork.com/">Hanleys of Cork</a>
                        </li>                         
                        <li><a href="https://www.fernhill.ie/">fernhill.ie</a>
                        </li>                         
                    </ul>                     
                </div>                 
            </section>             
            <!-- Category: Garden Centres in Canada -->             
            <section> 
                <h2>Garden Centres in Canada</h2> 
                <div class="description"> 
                    <p>
                        Explore the best garden centres across Canada, featuring a wide variety of plants, trees, and garden supplies. Enjoy personalized service and expert gardening tips to make the most of your outdoor space, whether it's a small balcony or a sprawling yard.
                    </p> 
                </div>                 
                <div class="websites"> 
                    <ul> 
                        <li><a href="https://www.gardenworks.ca/">gardenworks.ca</a>
                        </li>                         
                        <li><a href="https://www.lacostegardencentre.com/">lacostegardencentre.com</a>
                        </li>                         
                        <li><a href="https://www.gardenretreat.ca/">gardenretreat.ca</a>
                        </li>                         
                        <li><a href="https://www.oxfordinstashade.com/">oxfordinstashade.com</a>
                        </li>                         
                        <li><a href="https://www.littletreegardenmarket.ca/">littletreegardenmarket.ca</a>
                        </li>                         
                        <li><a href="https://www.greyhavengardens.com/">greyhavengardens.com</a>
                        </li>                         
                        <li><a href="https://www.buckerfields.ca/">buckerfields.ca</a>
                        </li>                         
                        <li><a href="https://www.waltergreenhouse.ca/">waltergreenhouse.ca</a>
                        </li>                         
                        <li><a href="https://www.tripletreenurseryland.com/">tripletreenurseryland.com</a>
                        </li>                         
                    </ul>                     
                </div>
            </section>             
            <!-- Category: Garden Centres in the United Kingdom -->             
            <section> 
                <h2>Garden Centres in the United Kingdom</h2> 
                <div class="description"> 
                    <p>
                        Visit United Kingdom-based garden centers that offer not only plants and equipment but also workshops and gardening expertise.                   </p> 
                </div>                 
                <div class="websites"> 
                    <ul> 
                        <li><a href="https://www.elmwoodgardencentre.co.uk/">elmwoodgardencentre.co.uk</a>
                        </li>                         
                        <li><a href="https://www.knightsgardencentres.com/">knightsgardencentres.com</a>
                        </li>                         
                        <li><a href="https://www.merryhatton.co.uk/">merryhatton.co.uk</a>
                        </li>                         
                        <li><a href="https://www.ripleynurseries.co.uk/">ripleynurseries.co.uk</a>
                        </li>                         
                        <li><a href="https://www.radwaybridgegardencentre.com/">radwaybridgegardencentre.com</a>
                        </li>                         
                        <li><a href="https://www.thirskgardencentre.co.uk/">thirskgardencentre.co.uk</a>
                        </li>                         
                        <li><a href="https://www.wellandvale.co.uk/">wellandvale.co.uk</a>
                        </li>                         
                        <li><a href="https://www.slemishlandscapecentre.com/">slemishlandscapecentre.com</a>
                        </li>                         
                        <li><a href="https://www.trioscape.co.uk/">trioscape.co.uk</a>
                        </li>                         
                        <li><a href="https://www.creativegardens.com/">creativegardens.com</a>
                        </li>
                        <li><a href="https://www.birkacre.co.uk/">birkacre.co.uk</a>
                        </li>
                        <li><a href="https://coblandsgardencentre.co.uk/">coblandsgardencentre.co.uk</a>
                        </li>
                        <li><a href="https://www.codsallandwergs.co.uk/">codsallandwergs.co.uk</a>
                        </li>
                        <li><a href="https://www.henrystreet.co.uk/">henrystreet.co.uk</a>
                        </li>
                        <li><a href="https://www.horticentre.co.uk/">horticentre.co.uk</a>
                        </li>
                        <li><a href="https://www.millbrookgc.co.uk/">millbrookgc.co.uk</a>
                        </li>
                        <li><a href="https://www.rushfields.com/">rushfields.com</a>
                        </li>
                        <li><a href="https://www.stewarts.co.uk/">stewarts.co.uk</a>
                        </li>
                        <li><a href="https://www.thompsons-plants.co.uk/">thompsons-plants.co.uk</a>
                        </li>
                    </ul>                     
                </div>
            </section>             
            <!-- Category: Tuincentrum leveranciers -->             
            <section> 
                <h2>Tuincentrum leveranciers</h2> 
                <div class="description"> 
                    <p>
                        Connect with top suppliers for garden centres in the Netherlands and Belgium. Offering a comprehensive range of plants, seeds, and gardening equipment, these suppliers ensure that garden centres are well-stocked with high-quality products.
                    </div>                 
                <div class="websites"> 
                    <ul> 
                        <li><a href="https://www.green-solutions.com/nl-nl">Green Solutions </a>

                    </ul>                     
                </div>
            </section>             
            <!-- Category: Tuin blogs Nederlands -->             
            <section> 
                <h2>Tuin blogs Nederlands</h2> 
                <div class="description"> 
                    <p>
                        Dive into the world of gardening with Dutch garden blogs. These blogs provide tips, inspiration, and advice on various gardening topics, including plant care, garden design, and sustainable practices, all written in Dutch.
                    </p> 
                </div>                 
                <div class="websites"> 
                    <ul> 
                        <li><a href="https://www.tuincentrumoverzicht.be/">tuincentrumoverzicht.be</a>
                        </li>                         
                        <li><a href="https://www.tuincentrumoverzicht.nl/">tuincentrumoverzicht.nl</a>
                        </li>                         
                        <li><a href="https://www.goodgardn.nl/">goodgardn.nl</a>
                        </li>                         
                        <li><a href="https://www.leefinjetuin.nl/">leefinjetuin.nl</a>
                        </li>                         
                        <li><a href="https://www.100procentgroen.eu/">100procentgroen.eu</a>
                        </li>                         
                        <li><a href="https://www.alleshuisentuin.nl/">alleshuisentuin.nl</a>
                        </li>                         
                        <li><a href="https://www.bloemschikmateriaal.eu/">bloemschikmateriaal.eu</a>
                        </li>                         
                        <li><a href="https://www.buiteninjebuurt.nl/">buiteninjebuurt.nl</a>
                        </li>                         
                        <li><a href="https://www.dekroononline.be/">dekroononline.be</a>
                        </li>                         
                        <li><a href="https://www.depuretuin.nl/">depuretuin.nl</a>
                        </li>                         
                        <li><a href="https://www.detuinkampioen.nl/">detuinkampioen.nl</a>
                        </li>                         
                        <li><a href="https://www.devrolijketuinder.nl/">devrolijketuinder.nl</a>
                        </li>                         
                        <li><a href="https://www.dutchgarden.eu/">dutchgarden.eu</a>
                        </li>                         
                        <li><a href="https://www.good-living.nl/">good-living.nl</a>
                        </li>                         
                        <li><a href="https://www.green-smile.nl/">green-smile.nl</a>
                        </li>                         
                        <li><a href="https://www.hetgroenenetwerk.nl/">hetgroenenetwerk.nl</a>
                        </li>                         
                        <li><a href="https://www.homeandgardendreams.nl/">homeandgardendreams.nl</a>
                        </li>                         
                        <li><a href="https://www.homeandgardenxl.nl/">homeandgardenxl.nl</a>
                        </li>                         
                        <li><a href="https://www.palmnet.nl/">palmnet.nl</a>
                        </li>                         
                        <li><a href="https://www.robtuinontwerp.nl/">robtuinontwerp.nl</a>
                        </li>                         
                        <li><a href="https://www.tuinartikelenwinkels.nl/">tuinartikelenwinkels.nl</a>
                        </li>                         
                        <li><a href="https://www.tuinierenwebwinkel.nl/">tuinierenwebwinkel.nl</a>
                        </li>                         
                        <li><a href="https://www.tuinieronline.nl/">tuinieronline.nl</a>
                        </li>                         
                        <li><a href="https://www.tuinmeubelen-online.nl/">tuinmeubelen-online.nl</a>
                        </li>                         
                        <li><a href="https://www.carice.eu/">carice.eu</a>
                        </li>                         
                    </ul>                     
                </div>
            </section>             
            <!-- Category: Tuin blogs Engels -->             
            <section> 
                <h2>Tuin blogs Engels</h2> 
                <div class="description"> 
                    <p>
                        Dive into English-language garden blogs filled with gardening tips, inspirational stories, and practical advice for garden enthusiasts.                                      </p> 
                </div>                 
                <div class="websites"> 
                    <ul>
                        <li>
                            <a href="https://www.gardenstreet.eu/">Tips For Gardening</a>
                        </li>
                        <li>
                            <a href="https://www.goodgardn.co.uk/">goodgardn.co.uk</a>
                        </li>
                        <li>
                            <a href="https://www.gardencenterguide.com/">gardencenterguide.com</a>
                        </li>
                        <li>
                            <a href="https://www.gardencentreguide.co.uk/">gardencentreguide.co.uk</a>
                        </li>
                        <li>
                            <a href="https://www.designgarden.eu/">designgarden.eu</a>
                        </li>
                        <li>
                            <a href="https://www.onlinegardeningcentre.co.uk/">onlinegardeningcentre.co.uk</a>
                        </li>
                        <li>
                            <a href="https://www.city-garden.eu/">city-garden.eu</a>
                        </li>
                        <li>
                            <a href="https://www.gardenexpert.eu/">gardenexpert.eu</a>
                        </li>
                        <li>
                            <a href="https://www.gardeningagency.co.uk/">gardeningagency.co.uk</a>
                        </li>
                        <li>
                            <a href="https://www.gardenretail.co.uk/">gardenretail.co.uk</a>
                        </li>
                        <li>
                            <a href="https://www.lifeplanters.eu/">lifeplanters.eu</a>
                        </li>
                        <li>
                            <a href="https://www.expertgardening.co.uk/">expertgardening.co.uk</a>
                        </li>
                        <li>
                            <a href="https://www.gardenclublistings.co.uk/">gardenclublistings.co.uk</a>
                        </li>
                        <li>
                            <a href="https://www.marchisio.eu/">marchisio.eu</a>
                        </li>
                        <li>
                            <a href="https://www.royalgardens.eu/">royalgardens.eu</a>
                        </li>
                    </ul>                     
                </div>
            </section>             
            <!-- Category: Webshops Nederland en Belgie -->             
            <section> 
                <h2>Webshops Nederland en Belgie</h2> 
                <div class="description"> 
                    <p>
                        Blader door online winkels in Nederland en België voor een uitgebreide selectie tuinproducten en accessoires.                                       </p> 
                </div>                 
                <div class="websites"> 
                    <ul>
                        <li>
                            <a href="https://www.bbqkopen.nl/">bbqkopen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.detuinwinkelonline.nl/">detuinwinkelonline.nl</a>
                        </li>
                        <li>
                            <a href="https://www.toptuincentrum.nl/">toptuincentrum.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincenter-vincent.be/">tuincenter-vincent.be</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumoutlet.com/">tuincentrumoutlet.com</a>
                        </li>
                        <li>
                            <a href="https://www.tuincollectie.nl/">tuincollectie.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuinmeubels.nl/">tuinmeubels.nl</a>
                        </li>
                    </ul>                     
                </div>
            </section>             
            <!-- Category: Tuincentra Nederland en Belgie -->             
            <section> 
                <h2>Tuincentra Nederland en Belgie</h2> 
                <div class="description"> 
                    <p>
                        Verken tuincentra in Nederland en België voor een uitgebreide selectie planten, gereedschappen en tuinadvies.                    </p> 
                </div>                 
                <div class="websites"> 
                    <ul>
                        <li>
                            <a href="https://www.graka.nl/">Tuincentrum Graka</a>
                        </li>
                        <li>
                            <a href="https://www.gardencenterwemmel.be/">gardencenterwemmel.be</a>
                        </li>
                        <li>
                            <a href="https://www.groencentrum.be/">groencentrum.be</a>
                        </li>
                        <li>
                            <a href="https://www.groencentrumwitmarsum.nl/">groencentrumwitmarsum.nl</a>
                        </li>
                        <li>
                            <a href="https://www.groengoedmenken.nl/">groengoedmenken.nl</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijkassen.nl/">groenrijkassen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijktilburg.nl/">groenrijktilburg.nl</a>
                        </li>
                        <li>
                            <a href="https://www.huisentuinhoogeveen.nl/">huisentuinhoogeveen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.jouw-tuin.nl/">jouw-tuin.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumdeoudetol.nl/">tuincentrumdeoudetol.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentruminterflower.be/">tuincentruminterflower.be</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumluyckx.be/">tuincentrumluyckx.be</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumoosterhout.nl/">tuincentrumoosterhout.nl</a>
                        </li>
                        <li>
                            <a href="https://www.poppelaarstuincentrum.nl/">poppelaarstuincentrum.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tcdedriesprong.nl/">https://www.tcdedriesprong.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tcdeschouw.nl/">tcdeschouw.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tctuinextra.nl/">tctuinextra.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumtullekensmolen.nl/">tuincentrumtullekensmolen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumverheijen.nl/">tuincentrumverheijen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumvriezen.nl/">tuincentrumvriezen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuinwereld-dordrecht.nl/">tuinwereld-dordrecht.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumbull.nl/">tuincentrumbull.nl</a>
                        </li>
                        <li>
                            <a href="https://www.beekertuincentrum.nl/">Beeker Tuincentrum Beek</a>
                        </li>
                        <li>
                            <a href="https://www.degroenevakwinkel-hoogerheide.nl/">De Groene Vakwinkel Hoogerheide</a>
                        </li>
                        <li>
                            <a href="https://www.dewilskracht.nl/">GroenRijk de Wilskracht Den Haag</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijkbenedenleeuwen.nl/">GroenRijk Beneden Leeuwen</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijkdenbosch.nl/">GroenRijk Den Bosch Tuincentrum</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijkgeldrop.nl/">GroenRijk Geldrop Tuincentrum</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijknieuwegein.nl/">GroenRijk Nieuwegein Tuincentrum</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijkveldhoven.nl/">GroenRijk Veldhoven Tuincentrum</a>
                        </li>
                        <li>
                            <a href="https://www.groenrijkzevenaar.nl/">GroenRijk Zevenaar​ Tuincentrum</a>
                        </li>
                        <li>
                            <a href="https://www.kwekerijsouman.nl/">Kwekerij en Tuincentrum Souman Hattem</a>
                        </li>
                        <li>
                            <a href="https://www.lifeandgardenetten-leur.nl/">Tuincentrum Life and Garden Etten-Leur</a>
                        </li>
                        <li>
                            <a href="https://www.lifeandgardenoostburg.nl/">Tuincentrum Life and Garden Oostburg</a>
                        </li>
                        <li>
                            <a href="https://www.lifeandgardenrenesse.nl/">Tuincentrum Life and Garden Renesse</a>
                        </li>
                        <li>
                            <a href="https://www.lokkemientje.nl/">Tuincentrum ’t Lokkemientje Edam</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumtuin.nl/">Tuincentrum Tuin! Zwaagwesteinde</a>
                        </li>
                        <li>
                            <a href="https://www.natuurlijktilburg.nl/">natuurlijktilburg.nl</a>
                        </li>
                        <li>
                            <a href="https://www.poppelaarskerstbomen.nl/">poppelaarskerstbomen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.poppelaarstuincentrum.nl/">poppelaarstuincentrum.nl</a>
                        </li>
                        <li>
                            <a href="https://www.rijkenbergtuinmeubelen.nl/">rijkenbergtuinmeubelen.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tcvanee.nl/">tuincentrum van Ee</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumbloemenland.be/">Tuincentrumbloemenland.be</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumborghuis.nl/">tuincentrumborghuis.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumdaniels.nl/">Tuincentrumdaniels.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumdebosrank.nl/">tuincentrumdebosrank.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuincentrumockenburgh.nl/">tuincentrumockenburgh.nl</a>
                        </li>
                        <li>
                            <a href="https://www.tuinwereld.nl/vestiging/tuinwereld-wijchen">Tuinwereld wijchen</a>
                        </li>
                        <li>
                            <a href="https://www.vandenbroekbestratingen.nl/">vandenbroekbestratingen.nl</a>
                        </li>
                    </ul>
                    <section> 
                        <h2>Dierenwinkels</h2> 
                        <div class="description"> 
                            <p>
                                Explore the best pet shops offering a wide range of products for your pets, including food, toys, grooming supplies, and accessories. Whether you have a dog, cat, bird, or reptile, these stores have everything you need to keep your pets happy and healthy.
                            </p> 
                        </div>                         
                        <div class="websites"> 
                            <ul>
                                <li><a href="https://www.dierenartsboschhoven.nl/">dierenartsboschhoven.nl</a>
                                </li>
                                <li><a href="https://www.dierenkliniekcoppelmans.nl/">dierenkliniekcoppelmans.nl</a>
                                </li>
                                <li><a href="https://www.petfooddiscount.nl/">petfooddiscount.nl</a>
                                </li>
				</li>
                                <li><a href="https://huisdierenvriend.com/">huisdierenvriend.com</a>
                                </li>
                            </ul>                             
                        </div>
                    </section>                     
                    <!-- Category: Divers -->                     
                    <section> 
                        <h2>Divers</h2> 
                        <div class="description"> 
                            <p>
                                Explore a diverse range of topics, products, and services that don't fit neatly into the other categories. From unique finds to unconventional offerings, this category is a treasure trove of surprises waiting to be discovered.
                            </p> 
                        </div>                         
                        <div class="websites"> 
                            <ul> 
                                <li><a href="https://www.dietistmandybreure.nl/leververvetting/">Insulineresistentie</a>
                                </li>     
                                  <li><a href="https://pijntherapie.com">pijntherapie.com</a>
                                </li>
                                </li>     
                                  <li><a href="https://wolfworldwide.digital">wolfworldwide.digital</a>
                                </li>
                                 </li>     
                                <li><a href="https://groweb.nl">groweb.nl</a>
                                </li>
                                </li>     
                                <li><a href="https://pijntherapie.com">pijntherapie.com</a>
                                  </li>
                                <li><a href="https://www.nationale-tuinbon.nl/">nationale-tuinbon.nl</a>
                                </li>                                 
                                <li><a href="http://www.mobihouse.nl/">mobihouse.nl</a>
                                </li>                                 
                                <li><a href="https://www.kunstkerstboompunt.nl/">kunstkerstboompunt.nl</a>
                                </li>                                 
                                <li><a href="https://www.kerstoutletonline.nl/">kerstoutletonline.nl</a>
                                </li>                                 
                                <li><a href="https://www.mrchristmasnl.nl/">mrchristmasnl.nl</a>
                                </li>                                 
                                <li><a href="https://www.onlinekerstshop.nl/">onlinekerstshop.nl</a>
                                </li>                                 
                                <li><a href="https://www.tuingereedschapshop.nl/">tuingereedschapshop.nl</a>
                                </li>                                 
                                <li><a href="https://www.delekkerstebbq.nl/">BBQ vergelijken</a>
                                </li>                                 
                                <li><a href="https://www.huisdierkoopjes.nl/">Huisdierkoopjes</a>
                                </li>                                 
                                <li><a href="https://www.onlinetuinmeubel.nl/">Online Tuinmeubels</a>
                                </li>
                                <li><a href="https://www.tuinmeubelsvoordeel.nl/">Tuinmeubels met voordeel</a>
          </ul>
        </div>
    </section>
</main>
"""