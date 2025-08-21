from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Trade
from .forms import TradeForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'trades/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trades = Trade.objects.filter(user=self.request.user)
        realized_trades = [t for t in trades if t.pnl is not None]
        total_pnl = sum((t.pnl for t in realized_trades)) if realized_trades else 0
        wins = sum(1 for t in realized_trades if t.pnl and t.pnl > 0)
        win_rate = (wins / len(realized_trades) * 100) if realized_trades else 0
        context.update({
            'trade_count': trades.count(),
            'realized_count': len(realized_trades),
            'total_pnl': total_pnl,
            'win_rate': win_rate,
        })
        return context


class TradeListView(LoginRequiredMixin, ListView):
    model = Trade
    template_name = 'trades/trade_list.html'

    def get_queryset(self):
        return Trade.objects.filter(user=self.request.user)


class TradeCreateView(LoginRequiredMixin, CreateView):
    model = Trade
    form_class = TradeForm
    template_name = 'trades/trade_form.html'
    success_url = reverse_lazy('trade-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TradeUpdateView(LoginRequiredMixin, UpdateView):
    model = Trade
    form_class = TradeForm
    template_name = 'trades/trade_form.html'
    success_url = reverse_lazy('trade-list')

    def get_queryset(self):
        return Trade.objects.filter(user=self.request.user)


class TradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Trade
    template_name = 'trades/trade_confirm_delete.html'
    success_url = reverse_lazy('trade-list')

    def get_queryset(self):
        return Trade.objects.filter(user=self.request.user)

# Create your views here.
