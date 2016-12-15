obj = {'jiang':'23'}
print(len(obj))
print(obj.get('jian',''))

print(len([]))

val = []
val.append(1)
val.append(2)
print(val)
va = (2,)
print(va[0])

import re
URL = 'http://8.wacai.com/list/wenying/p1'
re_obj = re.compile('([http:\/\/|https:\/\/].*\.\w+)')
print(re_obj.search(URL).group(1))
objs = r'([http:\/\/|https:\/\/].*\.\w+)'
print(type(objs))

ojs = []
print(len(ojs))

re_str = '([http:\\/\\/|https:\\/\\/].*\\.\\w+)'
domain_complie = re.compile(re_str)
print('domain==',[domain_complie.search('http://www.xiaoniu88.com/product/investment/30').group(1),])


test_html = '''
<ul class="box-sig">
			                        <li class="sig-l">
			                            <h1>
			                                <span class="til">


														<a href="/product/planning/detail/451504" title="安心牛D20160612-38028" target="_blank">安心牛D20160612-38028</a>



			                                </span>




			                                	<div title="<div class='forTransfer'>持有1个月后可转让<a href='http://www.xiaoniu88.com/portal/help/question/17/id/63' target='_blank'>了解详情</a></div>" class="zr">可转</div>









			                                	<div class="double12"></div>



												<div class="bouns12" title="<div class='forTransfer'>投资立即返现</div>"></div>




			                                	<div class="prize" data-producttype="3" data-specialarea="1" data-deadline="24" data-unit="1"></div>

			                            </h1>
			                            <div class="list-a">


			                            			<div class="list-a-1"><em class="rate">13.00-13.50</em><i>%</i></div>



			                            	<div class="list-a-2">预期年化收益率</div>
			                            </div>
			                            <div class="list-a">
			                            	<div class="list-a-1">



				                                		<em class="deadline">24</em>个月


			                                </div>
			                                <div class="list-a-2">期限</div>
			                            </div>
			                            <div class="list-a no-line">
			                            	<div class="list-a-1">



				                            		一次性还款


			                            	</div>
			                            	<div class="list-a-2">100元起投</div>
			                            </div>
									</li>





					                        		<li class="sig-r perform-to">
					                        			<span class="pt04">剩余金额：<strong>718,061</strong>元</span>
					                        			<a href="/product/planning/detail/451504" target="_blank">加  入</a>
					                        		</li>







								</ul>
								'''
from scrapy import Selector

sel_obj = Selector(text=test_html)
print(sel_obj.xpath("//li[@class='sig-l']/div/div/em[@class='deadline']/text()").extract())
